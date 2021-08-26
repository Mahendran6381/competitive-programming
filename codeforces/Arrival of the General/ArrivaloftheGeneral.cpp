#include <iostream>
using namespace  std;
int main() {
    int minVal=1000,minInd=0,maxVal=0,maxInd =0;
    int n,x =0;
    cin>>n;
    for(int i =0 ;i<n;i++){
        cin>>x;
        if(x > maxVal){
            maxInd =i;
            maxVal=x;
        }
        if(x <= minVal){
            minInd = i;
            minVal =x;
        }
    }
    std::cout << maxInd<<minInd << std::endl;
    if(maxInd>minInd){
       cout<<((maxInd-1)+(n-minInd))-1;
    }else{
        cout<<(maxInd-1)+(n-minInd);
    }
    return 0;
}