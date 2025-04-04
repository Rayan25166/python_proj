#include<stdio.h>
struct student
{
char name[20];
int roll_no;
int mark[10];
int total;
float avg;
};
int main()
{
int n,i,j;
printf("enter the no of students:\n");
scanf("%d",&n);
struct student stu[n];
for(i=0;i<n;i++)
{
printf("Name:\n");
scanf("%s",stu[i].name);
printf("Roll_no\n");
scanf("%d",&stu[i].roll_no);
for(j=0;j<3;j++)
{
printf("Enter the marks of %d subject",j+1);
scanf("%d",&stu[i].marks[j];
total=total+stu[i] marks[j];
}
stu[i].avg=total/3;
total=0;
}
for(i=0;i<n;i++)
{
printf("\n name:%srollno:%daverage:%f",stu[i].name,stu[i].roll no,stu[i].average);
}
return 0;
}


