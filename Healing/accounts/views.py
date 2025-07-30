from django.shortcuts import render, redirect
from django.http import HttpRequest
from Website.models import Specialist, Member
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

# --- Password Reset Views ---

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('accounts:password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


# --- Registration View ---

def register_type(request: HttpRequest):
    error_msg = ""
    
    if request.method == "POST":
        reg_type = request.POST.get("regType")
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        pwd = request.POST.get("password")
        pwd2 = request.POST.get("confirm_password")

        if not reg_type:
            error_msg = "يرجى اختيار نوع التسجيل"
        elif pwd != pwd2:
            error_msg = "كلمتا المرور غير متطابقتين"
        else:
            try:
                new_user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=pwd
                )
                full_name = f"{first_name} {last_name}".strip()

                if reg_type == "member":
                    Member.objects.create(
                        user=new_user,
                        member_name=full_name,
                        member_age=request.POST.get("member_age", "").strip(),
                        member_city=request.POST.get("member_city", "").strip()
                    )

                    try:
                        group = Group.objects.get(name="members")
                        new_user.groups.add(group)
                    except Group.DoesNotExist:
                        error_msg = "مجموعة المستخدمين غير موجودة (members)"
                        new_user.delete()
                        return render(request, "accounts/register_type.html", {'error_msg': error_msg})

                elif reg_type == "specialist":
                    Specialist.objects.create(
                        user=new_user,
                        specialist_name=full_name,
                        specialist_specialization=request.POST.get("specialist_specialization", "").strip(),
                        specialist_image=request.FILES.get("specialist_image"),
                        specialist_specialization_image=request.FILES.get("specialist_specialization_image"),
                        specialist_city=request.POST.get("specialist_city", "").strip(),
                        specialist_phone=request.POST.get("specialist_phone", "").strip(),
                        specialist_personal_page=request.POST.get("specialist_personal_page", "").strip(),
                        specialist_information=request.POST.get("specialist_information", "").strip(),
                    )
                else:
                    error_msg = "نوع التسجيل غير معروف"
                    new_user.delete()

                if not error_msg:
                    return redirect('accounts:login_user')

            except IntegrityError:
                error_msg = "اسم المستخدم موجود مسبقاً، يرجى اختيار اسم آخر"
            except Exception as e:
                print(e)
                error_msg = error_msg or "حدث خطأ أثناء المعالجة، حاول مرة أخرى لاحقاً"

    return render(request, "accounts/register_type.html", {'error_msg': error_msg})


# --- Login View ---

def login_user(request: HttpRequest):
    msg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("Website:home")
        else:
            msg = "بيانات الدخول غير صحيحة، تحقق من اسم المستخدم وكلمة المرور"

    return render(request, "accounts/login.html", {"msg": msg})


# --- Logout View ---

def logout_user(request: HttpRequest):
    logout(request)
    return redirect("Website:home")
