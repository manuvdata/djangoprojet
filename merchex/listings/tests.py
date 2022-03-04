from django.test import TestCase

# Create your tests here.
def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        with open('ffi.pickle', 'wb') as f: pickle.dump(uploaded_file, f, pickle.HIGHEST_PROTOCOL)

        assert isinstance(uploaded_file.name, object)

        fs = FileSystemStorage()
        print(uploaded_file)
        fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file)

    return render(request, 'listings/pb.html')