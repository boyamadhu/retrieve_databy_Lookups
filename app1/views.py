from django.shortcuts import render
from app1.models import *
# Create your views here.
from django.db.models import Q
def display(request):
    TO=emp.objects.all()
    TO=emp.objects.filter(ename='ALLEN')
    TO=emp.objects.exclude(ename='ALLEN')
    # FIELD LOOKUPS
    TO=emp.objects.filter(hiredate__gt='1981-04-01')
    TO=emp.objects.filter(hiredate__gte='1981-02-01')
    TO=emp.objects.filter(hiredate__lt='1981-02-01')
    TO=emp.objects.filter(hiredate__lte='1981-04-01')
    TO=emp.objects.filter(hiredate__gt='1981-04-01')
    # DATE LOOKUPS
    TO=emp.objects.filter(hiredate__year='1981')
    TO=emp.objects.filter(hiredate__month='02')
    TO=emp.objects.filter(hiredate__day='17')
    TO=emp.objects.filter(hiredate__year__gt='1980')
    TO=emp.objects.filter(hiredate__year__gte='1980')
    TO=emp.objects.filter(hiredate__year__lt='1981')
    TO=emp.objects.filter(hiredate__year__lte='1980')
    TO=emp.objects.filter(hiredate__month__gt='02')
    TO=emp.objects.filter(hiredate__day__lt='20')
    # LIKE OPERATORS
    TO=emp.objects.filter(ename__startswith='A')
    TO=emp.objects.filter(ename__endswith='h')
    # contains operator
    TO=emp.objects.filter(ename__contains='A')
    TO=emp.objects.filter(hiredate__contains='02')
    TO=emp.objects.filter(empno__contains='5')
    # IN operator
    TO=emp.objects.filter(ename__in=('smith',))
    TO=emp.objects.filter(deptno__in=('10','20'))
    # REGEX 
    TO=emp.objects.filter(ename__regex=r'[A-Z]\w{5}')
    d={'display':TO}

    return render(request,'first.html',d)

def display_dept(request):
    TO=dept.objects.all()
    d={'display':TO}
    return render(request,'second.html',d)

def update_emp(request):
    # you can update the records in two ways
    # 1.update method
    # 2.update_or_create method

    # emp.objects.filter(ename='smith').update(job='Salesman')// ONE ROW IS SATISFIED
    # emp.objects.filter(job='SALESMAN').update(mgr='1234')// MORE THAN ONE ROW IS SATISFIED
    # emp.objects.filter(job='TRACKER').update(mgr='1234')// ZERO ROWS ARE SATISFYING
    # emp.objects.all().update(sal='500')// UPDATES ALL ROWS


    # TO=dept.objects.get_or_create(deptno='40',dname='checking',loc='random')[0]
    # TO.save()
    # emp.objects.update_or_create(ename='madhav',defaults={'empno':'4','ename':'naveen','mgr':'321','hiredate':'1999-12-12','sal':'666','comm':'65','deptno':TO})
    # emp.objects.filter(job='WATCHMAN').delete()// DELETE THE SPECIFIC DATA
    # emp.objects.filter(ename='naveen').delete()// DELETE THE SPECIFIC DATA
    emp.objects.all().delete()
    d={'display':emp.objects.all()}
    return render(request,'first.html',d)
