from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
from . import serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


def index(request):
    header_top = models.HeaderTop.objects.all()
    header_center = models.HeaderCenter.objects.all()
    header_end = models.HeaderEnd.objects.all()
    header_slider = models.HeaderSlider.objects.all()

    main_one_top = models.MainOneTop.objects.all()
    main_one_left = models.MainOneLeft.objects.all()
    main_one_right = models.MainOneRight.objects.all()

    main_two_left = models.MainTwoLeft.objects.all()
    main_two_right = models.MainTwoRight.objects.all()

    main_thee_top = models.MainTheeTop.objects.all()
    main_thee_content = models.MainTheeContent.objects.all()

    main_four_top = models.MainFourTop.objects.all()
    main_four_left = models.MainFourLeft.objects.all()
    main_four_right = models.MainFourRight.objects.all()

    footer = models.Footer.objects.all()

    obj = {
        'header_top':header_top,
        'header_center':header_center,
        'header_end':header_end,
        'header_slider':header_slider,

        'main_one_top':main_one_top,
        'main_one_left':main_one_left,
        'main_one_right':main_one_right,

        'main_two_left':main_two_left,
        'main_two_right':main_two_right,

        'main_thee_top':main_thee_top,
        'main_thee_content':main_thee_content,

        'main_four_top':main_four_top,
        'main_four_left':main_four_left,
        'main_four_right':main_four_right,

        'footer':footer,
    }
    return render(request,'index.html',obj)


def admin(request):
    header_top = models.HeaderTop.objects.all()
    header_center = models.HeaderCenter.objects.all()
    header_end = models.HeaderEnd.objects.all()
    header_slider = models.HeaderSlider.objects.all()

    main_one_top = models.MainOneTop.objects.all()
    main_one_left = models.MainOneLeft.objects.all()
    main_one_right = models.MainOneRight.objects.all()

    main_two_left = models.MainTwoLeft.objects.all()
    main_two_right = models.MainTwoRight.objects.all()

    main_thee_top = models.MainTheeTop.objects.all()
    main_thee_content = models.MainTheeContent.objects.all()

    main_four_top = models.MainFourTop.objects.all()
    main_four_left = models.MainFourLeft.objects.all()
    main_four_right = models.MainFourRight.objects.all()

    footer = models.Footer.objects.all()

    obj = {
        'header_top':header_top,
        'header_center':header_center,
        'header_end':header_end,
        'header_slider':header_slider,

        'main_one_top':main_one_top,
        'main_one_left':main_one_left,
        'main_one_right':main_one_right,

        'main_two_left':main_two_left,
        'main_two_right':main_two_right,

        'main_thee_top':main_thee_top,
        'main_thee_content':main_thee_content,

        'main_four_top':main_four_top,
        'main_four_left':main_four_left,
        'main_four_right':main_four_right,

        'footer':footer,
    }
    return render(request,'admin.html',obj)




def meetings(request):
    header_top = models.HeaderTop.objects.all()
    header_center = models.HeaderCenter.objects.all()
    header_end = models.HeaderEnd.objects.all()

    obj = {
        'header_top':header_top,
        'header_center':header_center,
        'header_end':header_end,
    }
    return render(request,'meetings.html',obj)




def meeting_details(request):
    header_top = models.HeaderTop.objects.all()
    header_center = models.HeaderCenter.objects.all()
    header_end = models.HeaderEnd.objects.all()

    obj = {
        'header_top':header_top,
        'header_center':header_center,
        'header_end':header_end,
    }
    return render(request,'meeting-details.html',obj)



# Header CRUD start

def creat_header_top(request):
    if request.method == 'POST':
        form = forms.HeaderTopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderTopForm()
    return render(request,'form.html',{'form':form})

def update_header_top(request,head_id):
    head = get_object_or_404(models.HeaderTop,id=head_id)
    if request.method == 'POST':
        form = forms.HeaderTopForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderTopForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_header_top(request,head_id):
    head = get_object_or_404(models.HeaderTop,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_header_center(request):
    if request.method == 'POST':
        form = forms.HeaderCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderCenterForm()
    return render(request,'form.html',{'form':form})

def update_header_center(request,head_id):
    head = get_object_or_404(models.HeaderCenter,id=head_id)
    if request.method == 'POST':
        form = forms.HeaderCenterForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderCenterForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_header_center(request,head_id):
    head = get_object_or_404(models.HeaderCenter,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})



def creat_header_end(request):
    if request.method == 'POST':
        form = forms.HeaderEndForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderEndForm()
    return render(request,'form.html',{'form':form})

def update_header_end(request,head_id):
    head = get_object_or_404(models.HeaderEnd,id=head_id)
    if request.method == 'POST':
        form = forms.HeaderEndForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderEndForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_header_end(request,head_id):
    head = get_object_or_404(models.HeaderEnd,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})



def creat_header_slider(request):
    if request.method == 'POST':
        form = forms.HeaderSliderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderSliderForm()
    return render(request,'form.html',{'form':form})

def update_header_slider(request,head_id):
    head = get_object_or_404(models.HeaderSlider,id=head_id)
    if request.method == 'POST':
        form = forms.HeaderSliderForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderSliderForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_header_slider(request,head_id):
    head = get_object_or_404(models.HeaderSlider,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})

# Header end

# Main one start

def creat_main_one_top(request):
    if request.method == 'POST':
        form = forms.MainOneTopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneTopForm()
    return render(request,'form.html',{'form':form})

def update_main_one_top(request,head_id):
    head = get_object_or_404(models.MainOneTop,id=head_id)
    if request.method == 'POST':
        form = forms.MainOneTopForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneTopForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_one_top(request,head_id):
    head = get_object_or_404(models.MainOneTop,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_one_left(request):
    if request.method == 'POST':
        form = forms.MainOneLeftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneLeftForm()
    return render(request,'form.html',{'form':form})

def update_main_one_left(request,head_id):
    head = get_object_or_404(models.MainOneLeft,id=head_id)
    if request.method == 'POST':
        form = forms.MainOneLeftForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneLeftForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_one_left(request,head_id):
    head = get_object_or_404(models.MainOneLeft,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_one_right(request):
    if request.method == 'POST':
        form = forms.MainOneRightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneRightForm()
    return render(request,'form.html',{'form':form})

def update_main_one_right(request,head_id):
    head = get_object_or_404(models.MainOneRight,id=head_id)
    if request.method == 'POST':
        form = forms.MainOneRightForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneRightForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_one_right(request,head_id):
    head = get_object_or_404(models.MainOneRight,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})



# Main one end


# Main two start

def creat_main_two_left(request):
    if request.method == 'POST':
        form = forms.MainTwoLeftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTwoLeftForm()
    return render(request,'form.html',{'form':form})

def update_main_two_left(request,head_id):
    head = get_object_or_404(models.MainTwoLeft,id=head_id)
    if request.method == 'POST':
        form = forms.MainTwoLeftForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTwoLeftForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_two_left(request,head_id):
    head = get_object_or_404(models.MainTwoLeft,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_two_right(request):
    if request.method == 'POST':
        form = forms.MainTwoRightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTwoRightForm()
    return render(request,'form.html',{'form':form})

def update_main_two_right(request,head_id):
    head = get_object_or_404(models.MainTwoRight,id=head_id)
    if request.method == 'POST':
        form = forms.MainTwoRightForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTwoRightForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_two_right(request,head_id):
    head = get_object_or_404(models.MainTwoRight,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})

# Main Two End

# Main Thee Start

def creat_main_thee_top(request):
    if request.method == 'POST':
        form = forms.MainTheeTopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTheeTopForm()
    return render(request,'form.html',{'form':form})

def update_main_thee_top(request,head_id):
    head = get_object_or_404(models.MainTheeTop,id=head_id)
    if request.method == 'POST':
        form = forms.MainTheeTopForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTheeTopForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_thee_top(request,head_id):
    head = get_object_or_404(models.MainTheeTop,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_thee_content(request):
    if request.method == 'POST':
        form = forms.MainTheeContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTheeContentForm()
    return render(request,'form.html',{'form':form})

def update_main_thee_content(request,head_id):
    head = get_object_or_404(models.MainTheeContent,id=head_id)
    if request.method == 'POST':
        form = forms.MainTheeContentForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTheeContentForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_thee_content(request,head_id):
    head = get_object_or_404(models.MainTheeContent,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


# Main Thee End

# Main Four Start
def creat_main_four_top(request):
    if request.method == 'POST':
        form = forms.MainFourTopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainFourTopForm()
    return render(request,'form.html',{'form':form})

def update_main_four_top(request,head_id):
    head = get_object_or_404(models.MainFourTop,id=head_id)
    if request.method == 'POST':
        form = forms.MainFourTopForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainFourTopForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_four_top(request,head_id):
    head = get_object_or_404(models.MainFourTop,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_four_left(request):
    if request.method == 'POST':
        form = forms.MainFourLeftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainFourLeftForm()
    return render(request,'form.html',{'form':form})

def update_main_four_left(request,head_id):
    head = get_object_or_404(models.MainFourLeft,id=head_id)
    if request.method == 'POST':
        form = forms.MainFourLeftForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainFourLeftForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_four_left(request,head_id):
    head = get_object_or_404(models.MainFourLeft,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_four_right(request):
    if request.method == 'POST':
        form = forms.MainFourRightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainFourRightForm()
    return render(request,'form.html',{'form':form})

def update_main_four_right(request,head_id):
    head = get_object_or_404(models.MainFourRight,id=head_id)
    if request.method == 'POST':
        form = forms.MainFourRightForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainFourRightForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_four_right(request,head_id):
    head = get_object_or_404(models.MainFourRight,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})

# Main Four End


# Footer Start

def creat_footer(request):
    if request.method == 'POST':
        form = forms.FooterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.FooterForm()
    return render(request,'form.html',{'form':form})

def update_footer(request,head_id):
    head = get_object_or_404(models.Footer,id=head_id)
    if request.method == 'POST':
        form = forms.FooterForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.FooterForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_footer(request,head_id):
    head = get_object_or_404(models.Footer,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})

# Footer End
# API Start
# Header API Start
class HeaderTopAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.HeaderTop, id=head_id)
            serializers = serializer.HeaderTopSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.HeaderTop.objects.all()
        serializers = serializer.HeaderTopSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.HeaderTopSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.HeaderTop, id=head_id)
        serializers = serializer.HeaderTopSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.HeaderTop, id=head_id)
        serializers = serializer.HeaderTopSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.HeaderTop, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class HeaderCenterAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.HeaderCenter, id=head_id)
            serializers = serializer.HeaderCenterSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.HeaderCenter.objects.all()
        serializers = serializer.HeaderCenterSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.HeaderCenterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.HeaderCenter, id=head_id)
        serializers = serializer.HeaderCenterSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.HeaderCenter, id=head_id)
        serializers = serializer.HeaderCenterSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.HeaderCenter, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class HeaderEndAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.HeaderEnd, id=head_id)
            serializers = serializer.HeaderEndSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.HeaderEnd.objects.all()
        serializers = serializer.HeaderEndSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.HeaderEndSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, head_id):
        head = get_object_or_404(models.HeaderEnd, id=head_id)
        serializers = serializer.HeaderEndSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.HeaderEnd, id=head_id)
        serializers = serializer.HeaderEndSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.HeaderEnd, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class HeaderSliderAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.HeaderSlider, id=head_id)
            serializers = serializer.HeaderSliderSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.HeaderSlider.objects.all()
        serializers = serializer.HeaderSliderSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.HeaderSliderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.HeaderSlider, id=head_id)
        serializers = serializer.HeaderSliderSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.HeaderSlider, id=head_id)
        serializers = serializer.HeaderSliderSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.HeaderSlider, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
# Header API End
# Main One API Start
class MainOneTopAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainOneTop, id=head_id)
            serializers = serializer.HeaderTopSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainOneTop.objects.all()
        serializers = serializer.MainOneTopSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainOneTopSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.MainOneTop, id=head_id)
        serializers = serializer.MainOneTopSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainOneTop, id=head_id)
        serializers = serializer.MainOneTopSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainOneTop, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class MainOneLeftAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainOneLeft, id=head_id)
            serializers = serializer.MainOneLeftSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainOneLeft.objects.all()
        serializers = serializer.MainOneLeftSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainOneLeftSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.MainOneLeft, id=head_id)
        serializers = serializer.MainOneLeftSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainOneLeft, id=head_id)
        serializers = serializer.MainOneLeftSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainOneLeft, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MainOneRightAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainOneRight, id=head_id)
            serializers = serializer.MainOneRightSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainOneRight.objects.all()
        serializers = serializer.MainOneRightSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainOneRightSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, head_id):
        head = get_object_or_404(models.MainOneRight, id=head_id)
        serializers = serializer.MainOneRightSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainOneRight, id=head_id)
        serializers = serializer.MainOneRightSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainOneRight, id=head_id)

class MainTwoLeftAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainTwoLeft, id=head_id)
            serializers = serializer.MainTwoLeftSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainTwoLeft.objects.all()
        serializers = serializer.MainTwoLeftSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainTwoLeftSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.MainTwoLeft, id=head_id)
        serializers = serializer.MainTwoLeftSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainTwoLeft, id=head_id)
        serializers = serializer.MainTwoLeftSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainTwoLeft, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MainTwoRightAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainTwoRight, id=head_id)
            serializers = serializer.MainTwoRightSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainTwoRight.objects.all()
        serializers = serializer.MainTwoRightSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainTwoRightSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, head_id):
        head = get_object_or_404(models.MainTwoRight, id=head_id)
        serializers = serializer.MainTwoRightSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainTwoRight, id=head_id)
        serializers = serializer.MainTwoRightSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainTwoRight, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MainTheeTopAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainTheeTop, id=head_id)
            serializers = serializer.MainTheeTopSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainTheeTop.objects.all()
        serializers = serializer.MainTheeTopSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainTheeTopSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.MainTheeTop, id=head_id)
        serializers = serializer.MainTheeTopSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainTheeTop, id=head_id)
        serializers = serializer.MainTheeTopSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainTheeTop, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MainTheeContentAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainTheeContent, id=head_id)
            serializers = serializer.MainTheeContentSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainTheeContent.objects.all()
        serializers = serializer.MainTheeContentSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainTheeContentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, head_id):
        head = get_object_or_404(models.MainTheeContent, id=head_id)
        serializers = serializer.MainTheeContentSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainTheeContent, id=head_id)
        serializers = serializer.MainTheeContentSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainTheeContent, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class MainFourTopAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainFourTop, id=head_id)
            serializers = serializer.HeaderTopSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainFourTop.objects.all()
        serializers = serializer.MainFourTopSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainFourTopSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.MainFourTop, id=head_id)
        serializers = serializer.MainFourTopSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainFourTop, id=head_id)
        serializers = serializer.MainFourTopSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainFourTop, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MainFourLeftAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainFourLeft, id=head_id)
            serializers = serializer.MainFourLeftSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainFourLeft.objects.all()
        serializers = serializer.MainFourLeftSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainFourLeftSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, head_id):
        head = get_object_or_404(models.MainFourLeft, id=head_id)
        serializers = serializer.MainFourLeftSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainFourLeft, id=head_id)
        serializers = serializer.MainFourLeftSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainFourLeft, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MainFourRightAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.MainFourRight, id=head_id)
            serializers = serializer.MainFourRightSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.MainFourRight.objects.all()
        serializers = serializer.MainFourRightSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializers = serializer.MainFourRightSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, head_id):
        head = get_object_or_404(models.MainFourRight, id=head_id)
        serializers = serializer.MainFourRightSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, head_id):
        head = get_object_or_404(models.MainFourRight, id=head_id)
        serializers = serializer.MainFourRightSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, head_id):
        head = get_object_or_404(models.MainFourRight, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class FooterAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.Footer, id=head_id)
            serializers = serializer.HeaderTopSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.Footer.objects.all()
        serializers = serializer.FooterSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.FooterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.Footer, id=head_id)
        serializers = serializer.FooterSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.Footer, id=head_id)
        serializers = serializer.FooterSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.Footer, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)