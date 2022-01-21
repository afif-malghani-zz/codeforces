#include <stdio.h>
int main()
{
    int length;
    scanf("%i", &length);
    int count;
    count =0;
    for(int i=0;i<length;i++){
	    char string[100];
	    scanf("%s",string);
	    for(int j=0;j<100;j++){
		    if(string[j] == '\0'){break;}
		    else{count++;}
	    }
	    if(count>10){
		    printf("%c",string[0]);
		    printf("%i",count-2);
		    printf("%c",string[count-1]);
		    printf("\n");
	    }
	    else{
		    printf("%s",string);
		    printf("\n");
	    }
	    count = 0;
    }
    return 0;
}
