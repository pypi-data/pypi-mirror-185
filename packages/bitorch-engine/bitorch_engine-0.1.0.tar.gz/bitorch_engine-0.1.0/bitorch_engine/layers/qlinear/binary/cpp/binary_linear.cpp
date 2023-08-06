#include <torch/extension.h>
#include <vector>
#include <chrono>
#include <algorithm>
#include <iostream>

// variable, position, value
#define BIT_SET(var, pos, val) var |= (val << pos)

typedef uint32_t BINARY_WORD;
const int BITS_PER_BINARY_WORD (sizeof(BINARY_WORD) * CHAR_BIT);

#define UNROLLN 6


/**
* @brief binarize matrix
*
*/
inline void _get_binary_row(float* row, BINARY_WORD * b_row, int size){
    #pragma omp parallel for
    for (int i = 0; i < size; i+=BITS_PER_BINARY_WORD) {
      BINARY_WORD rvalue=0;
      BINARY_WORD sign;
      for (int j = 0;j < BITS_PER_BINARY_WORD; ++j) {
        sign = (row[i+j]>=0);
        BIT_SET(rvalue, j, sign);
      }
      b_row[i/BITS_PER_BINARY_WORD] = rvalue;
    }
}

/**
  * @brief binarize matrix column wise.
  * Loop unroll and using register vars.
  * ~30% performance improvement without openmp
  * compared with get_binary_col() method.
  */
inline void _get_binary_col_unrolled(float* col, BINARY_WORD * b_col, int n, int k){
    for(int y=0; y<(n/BITS_PER_BINARY_WORD); y++){
      BINARY_WORD * y_col_pt = &b_col[y*k];
      #pragma omp parallel for
      for(int x=0; x < k; x+=4){
        register BINARY_WORD rvalue0=0, rvalue1=0, rvalue2=0, rvalue3=0;

        for(int b=0; b<BITS_PER_BINARY_WORD; b+=4){
          register BINARY_WORD sign0, sign1, sign2, sign3, sign4, sign5, sign6, sign7,
          sign8, sign9, sign10, sign11, sign12, sign13, sign14, sign15;

          float* col_0 = &col[(y*BITS_PER_BINARY_WORD+b)*k + x];
          float* col_1 = &col[(y*BITS_PER_BINARY_WORD+b+1)*k + x];
          float* col_2 = &col[(y*BITS_PER_BINARY_WORD+b+2)*k + x];
          float* col_3 = &col[(y*BITS_PER_BINARY_WORD+b+3)*k + x];

          sign0 = (*col_0>=0);
          sign1 = (*col_1>=0);
          sign2 = (*col_2>=0);
          sign3 = (*col_3>=0);

          BIT_SET(rvalue0, b, sign0);
          BIT_SET(rvalue0, (b+1), sign1);
          BIT_SET(rvalue0, (b+2), sign2);
          BIT_SET(rvalue0, (b+3), sign3);

          sign4 = (*(col_0+1)>=0);
          sign5 = (*(col_1+1)>=0);
          sign6 = (*(col_2+1)>=0);
          sign7 = (*(col_3+1)>=0);

          BIT_SET(rvalue1, b, sign4);
          BIT_SET(rvalue1, (b+1), sign5);
          BIT_SET(rvalue1, (b+2), sign6);
          BIT_SET(rvalue1, (b+3), sign7);

          sign8 = (*(col_0+2)>=0);
          sign9 = (*(col_1+2)>=0);
          sign10 = (*(col_2+2)>=0);
          sign11 = (*(col_3+2)>=0);

          BIT_SET(rvalue2, b, sign8);
          BIT_SET(rvalue2, (b+1), sign9);
          BIT_SET(rvalue2, (b+2), sign10);
          BIT_SET(rvalue2, (b+3), sign11);

          sign12 = (*(col_0+3)>=0);
          sign13 = (*(col_1+3)>=0);
          sign14 = (*(col_2+3)>=0);
          sign15 = (*(col_3+3)>=0);

          BIT_SET(rvalue3, b, sign12);
          BIT_SET(rvalue3, (b+1), sign13);
          BIT_SET(rvalue3, (b+2), sign14);
          BIT_SET(rvalue3, (b+3), sign15);
        }
        BINARY_WORD * pnter = &y_col_pt[x];
        *pnter = rvalue0;
        *(pnter+1) = rvalue1;
        *(pnter+2) = rvalue2;
        *(pnter+3) = rvalue3;
      }
    }
}

inline void _xnor_gemm_unrolled(int M, int N, int K,
                        BINARY_WORD *A, int lda,
                        BINARY_WORD *B, int ldb,
                        float *C, int ldc){
  int m,k,n;
  #pragma omp parallel for
  for (m = 0; m < M; ++m) {
    #pragma omp parallel for
    for (k = 0; k < ((K / UNROLLN) * UNROLLN); k+=UNROLLN) {
      BINARY_WORD A_PART[UNROLLN];
      A_PART[0] = A[m*lda+k];
      A_PART[1] = A[m*lda+k+1];
      A_PART[2] = A[m*lda+k+2];
      A_PART[3] = A[m*lda+k+3];
      A_PART[4] = A[m*lda+k+4];
      A_PART[5] = A[m*lda+k+5];
      #pragma omp parallel for
      for (n = 0; n < N; ++n) {
        int popc[UNROLLN];
        popc[0] = __builtin_popcountl(A_PART[0] ^ B[(k+0)*ldb+n]);
        popc[1] = __builtin_popcountl(A_PART[1] ^ B[(k+1)*ldb+n]);
        popc[2] = __builtin_popcountl(A_PART[2] ^ B[(k+2)*ldb+n]);
        popc[3] = __builtin_popcountl(A_PART[3] ^ B[(k+3)*ldb+n]);
        popc[4] = __builtin_popcountl(A_PART[4] ^ B[(k+4)*ldb+n]);
        popc[5] = __builtin_popcountl(A_PART[5] ^ B[(k+5)*ldb+n]);
        C[m*ldc+n] += popc[0] + popc[1] + popc[2] + popc[3] + popc[4] + popc[5];
      }
    }

    #pragma omp parallel for
    for (k=(K / UNROLLN) * UNROLLN; k < K; ++k) {
      BINARY_WORD A_PART = A[m*lda+k];
      #pragma omp parallel for
      for (n = 0; n < N; ++n) {
        C[m * ldc + n] += __builtin_popcountl(A_PART ^ B[k * ldb + n]);
      }
    }
  }

  // convert to (+1,-1) based presentation form
  #pragma omp parallel for
  for (int i=0; i < M*N; i++) {
    C[i] = -(2*C[i] - BITS_PER_BINARY_WORD*K);
  }
}


torch::Tensor binary_linear_forward_unpacked_weight(
    torch::Tensor weights,
    BINARY_WORD* binary_row,
    int m,
    int n,
    int k,
    bool verbose) {

    auto output = torch::zeros({m, n});
    auto w_packed = torch::zeros({k*n/BITS_PER_BINARY_WORD});
    // NOTE: .contiguous() will physically reorder the tensor layout according to the C style,
    // which is important here, since we operate on the data pointers.
    // Only using the transpose function doesn't change the data pointer.
    weights = weights.transpose(0,1).contiguous();

    //====== processing time measure ======//
    std::chrono::time_point<std::chrono::high_resolution_clock> start, finish;
    std::chrono::duration<double> elapsed;
    if(verbose == true) start = std::chrono::high_resolution_clock::now();

    BINARY_WORD* binary_col = (BINARY_WORD*)(w_packed.data_ptr<float>());
    _get_binary_col_unrolled(weights.data_ptr<float>(), binary_col, k, n);

    if(verbose == true){
        finish = std::chrono::high_resolution_clock::now();
        elapsed = finish - start;
        std::cout << "C++ XNOR_W_BITPACK elapsed time: " << elapsed.count() << " s\n";
    }

//    // debug binary col
//    if(verbose == true){
//        std::cout << "Binary col (C++):" << std::endl;
//        int print_r = k*n/BITS_PER_BINARY_WORD > 10 ? 10 : k*n/BITS_PER_BINARY_WORD;
//        for(int i=0; i<print_r; i++){
//            std::cout << binary_col[i] << " ";
//        }
//        std::cout << std::endl;
//    }

    if(verbose == true) start = std::chrono::high_resolution_clock::now();

    _xnor_gemm_unrolled(m, n, k/BITS_PER_BINARY_WORD,
          binary_row, k/BITS_PER_BINARY_WORD,
          binary_col, n,
          output.data_ptr<float>(), n);

    if(verbose == true){
        finish = std::chrono::high_resolution_clock::now();
        elapsed = finish - start;
        std::cout << "C++ XNOR_GEMM elapsed time: " << elapsed.count() << " s\n";
    }
    return output;
}


// already bit-packed weights
torch::Tensor binary_linear_forward_binarized_weight(
    torch::Tensor weights,
    BINARY_WORD* binary_row,
    int m,
    int n,
    int k,
    bool verbose) {

    auto output = torch::zeros({m, n});
    BINARY_WORD* binary_col;

    //====== processing time measure ======//
    std::chrono::time_point<std::chrono::high_resolution_clock> start, finish;
    std::chrono::duration<double> elapsed;
    if(verbose == true) start = std::chrono::high_resolution_clock::now();

    // torch doesn't support uint32 yet, we thus use int64, thus needs to convert to uint32_t by hand.
    binary_col = new BINARY_WORD[k*n/BITS_PER_BINARY_WORD];
    long* binary_col_long = (long*)weights.data_ptr();
//        std::cout << "Binarized weights (C++):" << std::endl;
    #pragma omp parallel for
    for(int i=0; i<k*n/BITS_PER_BINARY_WORD; i++){
//            std::cout << binary_col_long[i] << " ";
        binary_col[i] = (BINARY_WORD)(binary_col_long[i] & 0xffffffff);
    }
//        std::cout << std::endl;
    if(verbose == true){
        finish = std::chrono::high_resolution_clock::now();
        elapsed = finish - start;
        std::cout << "int64 to uint32_t copy time: " << elapsed.count() << " s\n";
    }

    if(verbose == true) start = std::chrono::high_resolution_clock::now();

    _xnor_gemm_unrolled(m, n, k/BITS_PER_BINARY_WORD,
          binary_row, k/BITS_PER_BINARY_WORD,
          binary_col, n,
          output.data_ptr<float>(), n);

    if(verbose == true){
        finish = std::chrono::high_resolution_clock::now();
        elapsed = finish - start;
        std::cout << "C++ XNOR_GEMM elapsed time: " << elapsed.count() << " s\n";
    }

    delete[] binary_col;
    return output;
}


BINARY_WORD* get_binary_row(
    torch::Tensor input,
    torch::Tensor a_packed,
    int m,
    int n,
    int k,
    bool verbose){
    //====== processing time measure ======//
    std::chrono::time_point<std::chrono::high_resolution_clock> start, finish;
    std::chrono::duration<double> elapsed;
    if(verbose == true){
        using ns = std::chrono::nanoseconds;
        using get_time = std::chrono::steady_clock;
        start = std::chrono::high_resolution_clock::now();
    }

    BINARY_WORD* binary_row = (BINARY_WORD*)(a_packed.data_ptr<float>());
    _get_binary_row(input.data_ptr<float>(), binary_row, m*k);

    if(verbose == true){
        finish = std::chrono::high_resolution_clock::now();
        elapsed = finish - start;
        std::cout << "C++ XNOR_A_BITPACK elapsed time: " << elapsed.count() << " s\n";
    }

//    //debug binary row
//    if(verbose == true){
//        std::cout << "Binary row (C++):" << std::endl;
//        int print_r = m*k/BITS_PER_BINARY_WORD > 10 ? 10 : m*k/BITS_PER_BINARY_WORD;
//        for(int i=0; i<print_r; i++){
//            std::cout << binary_row[i] << " ";
//        }
//        std::cout << std::endl;
//    }
    return binary_row;
}

torch::Tensor binary_linear_forward(
    torch::Tensor input,
    torch::Tensor weights,
    int m,
    int n,
    int k,
    bool verbose) {

    auto a_packed = torch::zeros({m*k/BITS_PER_BINARY_WORD});
    auto output = torch::zeros({m, n});

    BINARY_WORD* binary_row = get_binary_row(input, a_packed, m, n, k, verbose);

    // uses the total number of weight elements to identify if it is already binarized
    if(weights.numel() == k*n/BITS_PER_BINARY_WORD) {
        return binary_linear_forward_binarized_weight(weights, binary_row, m, n, k, verbose);
    }else{
        return binary_linear_forward_unpacked_weight(weights, binary_row, m, n, k, verbose);
    }
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("forward", &binary_linear_forward, "binary linear forward");
}
