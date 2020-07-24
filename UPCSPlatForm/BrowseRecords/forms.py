# Begin
# auth:lzy
# create date:7.22
# description:评价表单


from django import forms


class RecordForm(forms.Form):
    thisRecord = forms.CharField(
        label="浏览记录", max_length=1024, min_length=1, widget=forms.Textarea(
            attrs={'rows': 5, 'required': "required"}
        )
    )

# End
