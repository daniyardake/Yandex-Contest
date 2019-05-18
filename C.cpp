#include <iostream>
#include <string>

using namespace std;

struct query{
  int min;
  int max;
};


string toRegular(string RLEString){
  string regularString, stringNumber;
  int num1;
  int i = 0;
  int j;

  while(i < RLEString.length() ){
    stringNumber = "";
    if(isdigit(RLEString[i]) ){
      j = i;
      while(isdigit(RLEString[j]) ){ j++;}
      stringNumber = RLEString.substr(i, j-i); //forming a number of chars

      num1 = stoi(stringNumber);
      regularString += string(num1, RLEString[j]);
      i = j+1;
    }
    else {
      regularString += RLEString[i];
      i++;
    }
  }

  return regularString;
}


string toRLE(string regularString){
  string RLEString;

  int counter;
  int j;
  int i = 0;
  while(i < regularString.length()){
    j = i;
    counter = 0;

    while(regularString[j]==regularString[j+1]){
      counter++;
      j++;
    }
    int n = counter +1;
    if(n>1){RLEString +=regularString[i] + to_string(n);}
    else {RLEString += regularString[i];}

    i = i + counter + 1;
  }
  return RLEString;
}

int main(){
  //INPUT*****************
  string inputRLEString;
  cin>>inputRLEString;

  int q;
  cin>>q;
  query bounds[q];
  for(int i = 0; i < q; i++){ cin>>bounds[i].min>>bounds[i].max;}
  //INPUT*****************

  string newString;
  //string regString =  toRegular(inputRLEString);
  
  for(int i = 0; i < q; i++){
    cout<<toRLE(toRegular(inputRLEString).substr(bounds[i].min-1, bounds[i].max - bounds[i].min+1)).length()<<endl;
  }
  return 0;
}
