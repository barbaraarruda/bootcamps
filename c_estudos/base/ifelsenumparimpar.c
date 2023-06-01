#include <stdio.h>
  int main(){
      int num,qpar=0,qimp=0;
      float res;
      do{
          printf("Introduza");
          scanf("%d",&num);
          if(num!=0){  
              res=num%2;        

              if(res==0){
                  qpar++;
              } else {
                  qimp++;
              }
          }
      }while((num!=0));
      printf("Pares -> %d\n", qpar);
}
