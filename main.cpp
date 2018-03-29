#include <iostream>
#include<cmath>;
using namespace std;

void palindrome(string x)
{
    int i;
    int j = x.length()-1 ;
    for (i=0 ; i<=(x.length()/2) ; i++)
    {
        if (x[i]==x[j])
            j=j-1;
        else
        {
            cout<<"not palindrome";
            break;
        }
    }
    if (i>x.length()/2)
        cout<<"palindrome";
}


int factorial(int y)
{
    int result = 1;
    for (; y!=0 ; y--)
        result = result * y;
    if (y==0)
        return(result);
}


string to_string (int num)
{
    string y;
    int i,x,z=1;
    for (i=1 ; num/i!=0 ; i=i*10 )
    {
    }
    while (i!=0)
    {
        x = num/i + '0';
        num = num % i;
        i = i/10;
        if (z!=1)
            y = y + char(x);
        z=2;
    }
    return(y);
}


long to_int (string num)
{
    long x = 0;
    int z,m=0;
    for (int i = (num.length())-1 ; i>=0 ; i--)
    {
        z=num[m]-'0';
        x=(z*pow(10,i))+x;
        m=m+1;
    }
    return(x);
}



int sorting (int num)
{
    string y = to_string(num);
    int z,min,know=0;
    string str;
    for (int j=0 ; j<y.length() ; j++)
    {
        min=9;
        for (int i=0 ; i<y.length() ; i++)
        {
            z=y[i]-'0';
            if (z<min)
            {
                min = z;
                know = i ;
            }
        }
        y[know]='9';
        string l = to_string(min) ;
        str=str+l;
    }
    int m = to_int(str);
    return(m);
}


int reverse_int (int num)
{
    string y = to_string(num);
    string str;
    for (int i=0 ; i<y.length() ; i++)
        str=y[i]+str;
    int z = to_int(str);
    return(z);
}



string reverse_string(string x)
{
    string str;
    for (int i = 0 ; i<x.length() ; i++)
        str = x[i]+str;
    return(str);
}


int absolute(int x)
{
    return(x>=0 ? x : -x); // ? if that then return -- : else then return
}

/*
int test(int &x) //& bta5od l value l aslya msh copy leha. lama ta5od copy msh hat2sr 3l aslya bs lw 5t l aslya hat2sr 3la l value.
{
    x=x+1;
    return (x);
}
*/

int main()
{
    cout<<to_int("22222222");
    return 0;
}
