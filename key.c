# include <stdio.h>
int main()
{
int i,n,pos=0,key,flag=0,a[20];
printf("Enter the number of elements");
scanf("%d",&n);
printf("Enter the elements");
for (i=0;i<n;i++)
	{
	scanf("%d",&a[i]);
	}
for (i=0;i<n;i++)
	{
	printf("%d\t",a[i]);
	}
printf("\n enter key");
scanf("%d",&key);
for (i=0;i+<n;i++)
	{
	if(a[i]==key)
		{
		flag=1;
		pos=i;
		break;
		}
	}
if (flag==0)
	{
	printf("Element not found\n");
	}
else
	{
	printf("Element %d is found at %d\n",key,pos);
	}
return 0;
}
