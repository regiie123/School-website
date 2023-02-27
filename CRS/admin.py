from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import *


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'firstName', 'middleName', 'lastName')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'firstName', 'middleName',
                  'lastName', 'is_active', 'is_admin', 'is_chairperson', 'is_faculty', 'is_student')


class FacultyInfoInline(admin.StackedInline):
    # To add fields from Faculty database to User creation in Admin Site
    model = FacultyInfo
    can_delete = False
    verbose_name_plural = 'Faculty Profile'
    fk_name = 'facultyUser'


class StudentInfoInline(admin.StackedInline):
    # To add fields from Faculty database to User creation in Admin Site
    model = StudentInfo
    can_delete = False
    verbose_name_plural = 'Student Profile'
    fk_name = 'studentUser'


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    inlines = [FacultyInfoInline, StudentInfoInline]  # Add other InLine for cperson, student, etc...

    ''' The fields to be used in displaying the User model.
     These override the definitions on the base UserAdmin
     that reference specific fields on auth.User.
     '''
    list_display = ('email', 'firstName', 'middleName', 'lastName',
                    'is_active', 'is_admin', 'is_chairperson', 'is_faculty', 'is_student')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstName', 'middleName', 'lastName')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_chairperson', 'is_faculty', 'is_student')}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',
                       'firstName', 'middleName', 'lastName', 'is_admin', 'is_chairperson', 'is_faculty', 'is_student'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# CHAIRPERSON ADMIN
class ChairpersonInfoAdmin(admin.ModelAdmin):
    model = ChairpersonInfo
    list_display = ('get_id', 'get_email', 'get_lname', 'get_fname', 'get_mname')

    def get_email(self, obj):
        return obj.cpersonUser.email

    get_email.short_description = 'Email'

    def get_id(self, obj):
        return obj.cpersonUser.id

    get_id.short_description = 'ID'

    def get_fname(self, obj):
        return obj.cpersonUser.firstName

    get_fname.short_description = 'First Name'

    def get_lname(self, obj):
        return obj.cpersonUser.lastName

    get_lname.short_description = 'Last Name'

    def get_mname(self, obj):
        return obj.cpersonUser.middleName

    get_mname.short_description = 'Middle Name'


admin.site.register(RoomSchedule)
admin.site.register(RoomInfo)
admin.site.register(SubjectSchedule)


# FACULTY ADMIN
class FacultyInfoAdmin(admin.ModelAdmin):
    model = FacultyInfo
    list_display = ('get_id', 'get_email', 'get_lname', 'get_fname', 'get_mname')

    def get_email(self, obj):
        return obj.facultyUser.email

    get_email.short_description = 'Email'

    def get_id(self, obj):
        return obj.facultyUser.id

    get_id.short_description = 'ID'

    def get_fname(self, obj):
        return obj.facultyUser.firstName

    get_fname.short_description = 'First Name'

    def get_lname(self, obj):
        return obj.facultyUser.lastName

    get_lname.short_description = 'Last Name'

    def get_mname(self, obj):
        return obj.facultyUser.middleName

    get_mname.short_description = 'Middle Name'


# STUDENT ADMIN
class StudentInfoAdmin(admin.ModelAdmin):
    model = StudentInfo
    list_display = ('get_id', 'get_email', 'get_lname', 'get_fname', 'get_mname',)

    def get_email(self, obj):
        return obj.studentUser.email

    get_email.short_description = 'Email'

    def get_id(self, obj):
        return obj.studentUser.id

    get_id.short_description = 'ID'

    def get_fname(self, obj):
        return obj.studentUser.firstName

    get_fname.short_description = 'First Name'

    def get_lname(self, obj):
        return obj.studentUser.lastName

    get_lname.short_description = 'Last Name'

    def get_mname(self, obj):
        return obj.studentUser.middleName

    get_mname.short_description = 'Middle Name'


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# Register ProfileInfo and ProfileInfoAdmin
admin.site.register(ChairpersonInfo, ChairpersonInfoAdmin)
admin.site.register(FacultyInfo, FacultyInfoAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(AcademicYearInfo)
admin.site.register(BlockSection)
admin.site.register(subjectInfo),
admin.site.register(curriculumInfo),
admin.site.register(currchecklist),
admin.site.register(HD_DroppingForm),
admin.site.register(FacultyApplicant),
admin.site.register(hdClearanceForm)
admin.site.register(hdTransferCert)
admin.site.register(hdApplicant)
admin.site.register(OjtApplicant),
admin.site.register(spApplicant),
admin.site.register(LOAApplicant),
admin.site.register(ShifterApplicant),
admin.site.register(TransfereeApplicant),
admin.site.register(crsGrade),
admin.site.register(studentScheduling),

#DON'T TOUCH ^^
admin.site.site_header = 'iPLM Admin Site'
admin.site.index_title = 'Database Tables'
admin.site.site_title = 'iPLM Administration'

#Study Plan brrt brrt
class CurriculaAdmin(admin.ModelAdmin):
    search_fields = ['departmentID__courseName', 'cYear']

class courseListAdmin(admin.ModelAdmin):
    list_display = ['get_departmentID', 'courseCode', 'courseName', 'courseUnit', 'prerequisite', 'counted_in_GWA']

    def get_departmentID(self, obj):
        return obj.curricula.departmentID
    get_departmentID.admin_order_field = 'curricula__departmentID'
    get_departmentID.short_description = 'Department'

    search_fields = ['curricula__departmentID__courseName', 'courseCode', 'courseName']

admin.site.register(Curricula, CurriculaAdmin),
admin.site.register(courseList, courseListAdmin),
admin.site.register(studyPlan),