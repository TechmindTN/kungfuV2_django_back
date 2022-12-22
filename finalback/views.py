from cgi import print_form
import os
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
import profile
from datetime import date
from django.http.response import HttpResponseNotAllowed
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import get_user_model
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication

from finalback.models import  (
    Arbitrator,
    Username,
    ArchivedLicences,
    Coach,
    Athlete,
    Club,
    Image,
    Profile,
    Supporter,
    Competition,
    Match,
    Bracket,
    Result,
    role,
    Categorie,
    Grade,
    Licences,
    Weights,
    Ligue,
    Seasons,
    Degree,
    Discipline

)
from .serializers import  (
    ArbitratorSerializer,
    CoachSerializer,
    UsernameSerializer,
    ArchivedLicencesSerializer,
    AthleteSerializer,
    ClubSerializer,
    CompetitionSerializer,
    LigueSerializer,
    ImageSerializer,
    ResultSerializer,
    MatchSerializer,
    BracketSerializer,
    ProfileSerializer,
    RegisterSerializer,
    RoleSerializer,
    SupporterSerializer,
    UserSerializer,
    CategorieSerializer,
    LicencesSerializer,
    GradeSerializer,
    SeasonsSerializer,
    WeightSerializer,
    DegreeSerializer,
    DisciplineSerializer

)
#exel
import xlwt
import csv

from django.http import HttpResponse
from django.contrib.auth.models import User

def serialize_user(user):
    return {
        "id":user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
        
    }




@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })
        

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })


#just for testing the token (ichouf ken el user mte3ou)
@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_info': {
                "id":user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                #"location" : profile.location
                
            }
        })  
    return Response({'error':'token'}, status=400)


class DisciplineList(generics.ListCreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   

class RoleList(generics.ListCreateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class BracketList(generics.ListCreateAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BracketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class ResultList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResultDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArbitratorList(generics.ListCreateAPIView):
    queryset = Arbitrator.objects.all()
    serializer_class = ArbitratorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArbitratorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Arbitrator.objects.all()
    serializer_class = ArbitratorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CoachList(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CoachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LigueList(generics.ListCreateAPIView):
    queryset = Ligue.objects.all()
    serializer_class = LigueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LigueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ligue.objects.all()
    serializer_class = LigueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AthleteList(generics.ListCreateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClubList(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SupporterList(generics.ListCreateAPIView):
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SupporterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# csv
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response
#exel
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArchivedList(generics.ListCreateAPIView):
    queryset = ArchivedLicences.objects.all()
    serializer_class = ArchivedLicencesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArchivedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArchivedLicences.objects.all()
    serializer_class = ArchivedLicencesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CategorieList(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategorieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LicencesList(generics.ListCreateAPIView):
    queryset = Licences.objects.all()
    serializer_class = LicencesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LicencesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Licences.objects.all()
    serializer_class = LicencesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SeasonsList(generics.ListCreateAPIView):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SeasonsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WeightsList(generics.ListCreateAPIView):
    queryset = Weights.objects.all()
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WeightsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weights.objects.all()
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class DegreeList(generics.ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class UsernameList(generics.ListCreateAPIView):
    queryset = Username.objects.all()
    serializer_class = UsernameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UsernameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Username.objects.all()
    serializer_class = UsernameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



@csrf_exempt
def pro_list(request):
    """
    List all code snippets, or create a new Profile.
    """
    try:    
        if request.method == 'GET':
            userb =User.objects.all()
            profiles = Profile.objects.all()
            serializer = ProfileSerializer(profiles , many=True)
            if serializer.is_valid:
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({
                    "message":serializer.errors
                    }, safe=False,status=400)  
    except Exception as e:
        return JsonResponse({
                    "message":"There was a problem please try again later",
                    "error":str(e)
                    }, safe=False,status=500)  
          
@api_view(['GET'])
@csrf_exempt
def user_info(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """

    if request.method == 'GET':        
        user = User.objects.filter(id=pk)
        userserializer = UserSerializer(user, many=True)
        ok=False
        profile = Profile.objects.all()
        try:
            for p in profile:
                print(p.user)
                if p.user:
                    if p.user.pk==pk: 

                        print('a')
                
                        profileserializer = ProfileSerializer(p, many=False)
                    # info.append(userserializer.data)
                        info=profileserializer.data
                        ok=True
                        break
            if ok:
                return JsonResponse(info, safe=False)
            else :
                return JsonResponse([], safe=False)
        except:
            return Response({'Problem':'Problem'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def user_licences(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    if request.method == 'GET':       
        try:
            licences = Licences.objects.filter(user=pk)
            licenceserializer = LicencesSerializer(licences, many=True)
            if licenceserializer.is_valid:
                return JsonResponse(licenceserializer.data,safe=False)
            else:
                return JsonResponse({
                    "message":licenceserializer.errors
                    }, safe=False,status=400)  
        except Exception as e:
            return JsonResponse({
                        "message":"There was a problem please try again later"
                        }, safe=False,status=500)    
        
        
        
       
       
@api_view(['GET'])
@csrf_exempt
def parameters(request):
    """
    Retrieve, update or delete a code Profile.
    """
    if request.method == 'GET':       
        try:
            grades = Grade.objects.all()
            gradesSerializer = GradeSerializer(grades, many=True)
            categorie = Categorie.objects.all()
            categorieSerializer = CategorieSerializer(categorie, many=True)
            weights = Weights.objects.all()
            weightSerializer = WeightSerializer(weights, many=True)
            degrees = Degree.objects.all()
            degreeSerializer = DegreeSerializer(degrees, many=True)
            seasons = Seasons.objects.all()
            seasonSerializer = SeasonsSerializer(seasons, many=True)
            clubs = Club.objects.all()
            clubSerializer = ClubSerializer(clubs, many=True)
            disciplins = Discipline.objects.all()
            disciplineSerializer = DisciplineSerializer(disciplins, many=True)
            r = role.objects.all()
            roleSerializer = RoleSerializer(r, many=True)
                        
            parameters={
                        "Grades":gradesSerializer.data,
                        "Categories":categorieSerializer.data,
                        "Weights":weightSerializer.data,
                        "Degrees":degreeSerializer.data,
                        "Seasons":seasonSerializer.data,
                        "Clubs":clubSerializer.data,
                        "Disciplines":disciplineSerializer.data,
                        "Roles":roleSerializer.data
                        }
            return JsonResponse(parameters,safe=False)
        except Exception as e:
            
            return Response({'message':'There was a problem please try again later',
                             'error':str(e)
                             },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def verify_licence(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'PUT':    
                print(pk)   
            # try:
                licences = Licences.objects.filter(num_licences=pk).first()
                # licences.verified=True
                data = {"verified": True,
                        "state":"Verifiee"
                        }
                
                licenceserializer = LicencesSerializer(licences,data=data, partial=True)
                if licenceserializer.is_valid():
                    licenceserializer.save()
                    return JsonResponse(licenceserializer.data,safe=False)
                else:
                    return Response({'message':licenceserializer.errore},status=400)
    except Exception as e:
        return Response({'message':'There was a problem please try again later',
                         'error':str(e)
                         },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
     
     
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def validate_licence(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'PUT':       
            # try:
                licences = Licences.objects.filter(num_licences=pk).first()
                # licences.verified=True
                data = {"activated": True,
                        "state":"Activee"
                        }
                
                licenceserializer = LicencesSerializer(licences,data=data, partial=True)
                if licenceserializer.is_valid():
                    licenceserializer.save()
                    return JsonResponse(licenceserializer.data,safe=False)
                else:
                    return Response({'message':licenceserializer.errore},status=400)
    except Exception as e:
        return Response({'message':'There was a problem please try again later',
                         'error':str(e)
                         },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
           
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def club_licences(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':       
            # try:
                licences = Licences.objects.filter(club=pk)
                # licences.verified=True
                
                
                licenceserializer = LicencesSerializer(licences,many=True)
                if licenceserializer.is_valid:
                    return JsonResponse(licenceserializer.data,safe=False)
                else:
                    return Response({'message':licenceserializer.errore},status=400)
    except Exception as e:
        return Response({'message':'There was a problem please try again later',
                         'error':str(e)
                         },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # except:
        #     return Response({'Problem':'Problem'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def check_licence(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':       
            # try:
                licences = Licences.objects.filter(num_licences=pk)
                # licences.verified=True
                
                
                licenceserializer = LicencesSerializer(licences,many=True)
                if licenceserializer.is_valid:
                    return JsonResponse(licenceserializer.data,safe=False)
                else:
                    return Response({'message':licenceserializer.errore},status=400)
    except Exception as e:
        return Response({'message':'There was a problem please try again later',
                         'error':str(e)
                         },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
           
        # except:
        #     return Response({'Problem':'Problem'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def add_licence(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'POST':       
            # try:
                data=request.data
                licences = Licences.objects.last()
                num=str(int(licences.num_licences.split('-')[1])+1)
                for i in range(len(num),10,1):
                    num="0"+num
                
                data['num_licences']='AT-'+num
                licence=LicencesSerializer(data=request.data)
                
                if licence.is_valid():
                    licence.save()
                    return JsonResponse(licence.data,safe=False)
                else:
                    return Response({'message':licenceserializer.errore},status=400)
    except Exception as e:
        return Response({'message':'There was a problem please try again later',
                         'error':str(e)
                         },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             
            
            
            # # licences.verified=True
            
            
            # licenceserializer = LicencesSerializer(licences,many=True)
            
            # return JsonResponse(licenceserializer.data,safe=False)
           
        # except:
        #     return Response({'Problem':'Problem'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def renew_licence(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'PUT':       
            # try:
            licences = Licences.objects.filter(num_licences=pk).first()
            if licences.activated==True and licences.state=="Activee":
                season=Seasons.objects.filter(id=licences.seasons.pk).first()
                if season.activated==False:      
                    archivedLicece=   {                 
                            "role":licences.role.pk,
                            "num_licences":licences.num_licences,
                            "state":"Expired",
                            "user":licences.user.pk,
                            "seasons":licences.seasons.pk,
                            "grade":licences.grade.pk,
                            "weight":licences.weight.pk,
                            "categorie":licences.categorie.pk,
                            "club":licences.club.pk,
                            "discipline":licences.discipline.pk,
                            "degree":licences.degree.pk,
                            "verified":licences.verified,
                            "activated":False}
                    archiveSerializer= ArchivedLicencesSerializer(data=archivedLicece)
                    if archiveSerializer.is_valid():
                        archiveSerializer.save()
                        licenceserializer = LicencesSerializer(licences,data=request.data, partial=True)                      
                        if licenceserializer.is_valid():
                            licenceserializer.save()
                            return JsonResponse(licenceserializer.data,safe=False)
                        else:
                            return JsonResponse({'message':licenceserializer.errors})
                    else:
                        print(archiveSerializer._errors)
                        return JsonResponse({'message':archiveSerializer._errors},status=400)
                else:
                    return JsonResponse({"active season":"You can't renew a licence from the activated season"})
            else:
                return JsonResponse({"Inactive Licence":"You can't renew a licence with an inactive state"})
    except Exception as e:
        return JsonResponse({'message':'There was a problem please try again later',
                                 "error":str(e)
                                 },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
        
        

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def comp_info(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':        
            comp = Competition.objects.filter(id=pk).first()
            compSerializer = CompetitionSerializer(comp, many=False)
            tempdata=compSerializer.data
            age = Categorie.objects.filter(id=comp.age.pk).first()
            ageSerializer = CategorieSerializer(age, many=False)
            tempdata['age']=age.categorie_age
            season = Seasons.objects.filter(id=comp.season.pk).first()
            seasonSerializer = SeasonsSerializer(season, many=False)
            tempdata['season']=season.Seasons
            ligue = Ligue.objects.filter(id=comp.ligue.pk).first()
            ligueSerializer =LigueSerializer(ligue, many=False)
            tempdata['ligue']=ligue.name
            manager = User.objects.filter(id=comp.manager.pk).first()
            userSerializer =UserSerializer(manager, many=False)
            tempdata['manager']=manager.username
            discipline = Discipline.objects.filter(id=comp.discipline.pk).first()
            discSerializer =DisciplineSerializer(discipline, many=False)
            tempdata['discipline']=discipline.name
            return JsonResponse(tempdata,safe=False)
    except Exception as e:
        return JsonResponse({'message':'There was a problem please try again later',
                             'error':str(e)
                             },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
            

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def create_manager(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'POST': 
            data=request.data
            
                
            # data['num_licences']='AT-'+num
            user=UserSerializer(data=request.data)
                
            if user.is_valid():
                user.save()
                print(user.data['id'])
                print(user.id)
                # data={"user":user.id}
                return JsonResponse(user.data,safe=False)
            else:
                return JsonResponse({'message':user._errors},status=400)
                
    except Exception as e:
        return JsonResponse({'message':'There was a problem please try again later',
                             'error':str(e)
                             },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def role_licences(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    if request.method == 'GET':       
        try:
            licences = Licences.objects.filter(role=pk,activated=True)
            licenceserializer = LicencesSerializer(licences, many=True)
            if licenceserializer.is_valid:
                return JsonResponse(licenceserializer.data,safe=False)
            else:
                return JsonResponse({"message":licenceserializer.errors},
                                    status=400)
        except Exception as e:
            return Response({'message':'There was a problem please try again later',
                             'error':str(e)
                             },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def licence_info(request, pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':        
            licence = Licences.objects.filter(num_licences=pk).first()
            licenceSerializer = LicencesSerializer(licence, many=False)
            tempdata=licenceSerializer.data
            categorie = Categorie.objects.filter(id=licence.categorie.pk).first()
            ageSerializer = CategorieSerializer(categorie, many=False)
            tempdata['categorie']=categorie.categorie_age
            season = Seasons.objects.filter(id=licence.seasons.pk).first()
            seasonSerializer = SeasonsSerializer(season, many=False)
            tempdata['seasons']=season.Seasons
            degree = Degree.objects.filter(id=licence.degree.pk).first()
            degreeSerializer =DegreeSerializer(degree, many=False)
            tempdata['degree']=degree.Degree
            discipline = Discipline.objects.filter(id=licence.discipline.pk).first()
            discSerializer =DisciplineSerializer(discipline, many=False)
            tempdata['discipline']=discipline.name
            r = role.objects.filter(id=licence.role.pk).first()
            roleSerializer =RoleSerializer(r, many=False)
            tempdata['role']=r.roles
            weight = Weights.objects.filter(id=licence.weight.pk).first()
            weightSerializer =WeightSerializer(weight, many=False)
            tempdata['weight']=weight.masse_en_killograme
            grade = Grade.objects.filter(id=licence.grade.pk).first()
            gradeSerializer =GradeSerializer(grade, many=False)
            tempdata['grade']=grade.Grade
            club = Club.objects.filter(id=licence.club.pk).first()
            clubSerializer =ClubSerializer(club, many=False)
            tempdata['club']=club.name
            user = User.objects.filter(id=licence.user.pk).first()
            userserializer = UserSerializer(user, many=False)
            profile = Profile.objects.filter(user=user.pk).first()
            profileSerializer =ProfileSerializer(profile, many=False)
            tempdata['user']=profileSerializer.data
            if r!=None and profile!=None:
                        if r.pk==1:
                            arbitrator=Arbitrator.objects.filter(profile=profile.pk).first()
                            arbitratorSerializer=ArbitratorSerializer(arbitrator,many=False)
                            tempdata['arbitrator']=arbitratorSerializer.data
                        elif r.pk==2:
                            athlete=Athlete.objects.filter(profile=profile.pk).first()
                            athleteSerializer=AthleteSerializer(athlete,many=False)
                            tempdata['athlete']=athleteSerializer.data
                        elif r.pk==3:
                            supporter=Supporter.objects.filter(profile=profile.pk).first()
                            supporterSerializer=SupporterSerializer(supporter,many=False)
                            tempdata['supporter']=supporterSerializer.data
                        elif r.pk==4:
                            coach=Coach.objects.filter(profile=profile.pk).first()
                            coachSerializer=CoachSerializer(coach,many=False)
                            tempdata['coach']=coachSerializer.data
                    
            return JsonResponse(tempdata,safe=False)
        
        
        
        
        if request.method == 'PUT':
            licence=Licences.objects.filter(num_licences=pk).first()
            profile=Profile.objects.filter(user=licence.user.pk).first()
            if licence.role!=None and profile!=None:
                        if licence.role.pk==1:
                            arbitrator=Arbitrator.objects.filter(profile=profile.pk).first()
                            arbitratorSerializer=ArbitratorSerializer(arbitrator,data=request.data['arbitrator'],partial=True)
                            if arbitratorSerializer.is_valid():
                                arbitratorSerializer.save()
                            else:
                                return JsonResponse({'message':arbitratorSerializer.errors},status=400)
                            # arbitratorSerializer=ArbitratorSerializer(arbitrator,many=False)
                            # tempdata['arbitrator']=arbitratorSerializer.data
                        elif licence.role.pk==2:
                            athlete=Athlete.objects.filter(profile=profile.pk).first()
                            athleteSerializer=AthleteSerializer(athlete,data=request.data['athlete'],partial=True)
                            if athleteSerializer.is_valid():
                                athleteSerializer.save()
                            else:
                                return JsonResponse({'message':athleteSerializer.errors},status=400)
                            # athleteSerializer=AthleteSerializer(athlete,many=False)
                            # tempdata['athlete']=athleteSerializer.data
                        elif licence.role.pk==3:
                            supporter=Supporter.objects.filter(profile=profile.pk).first()
                            supporterSerializer=SupporterSerializer(supporter,data=request.data['supporter'],partial=True)
                            if supporterSerializer.is_valid():
                                supporterSerializer.save()
                            else:
                                return JsonResponse({'message':arbitratorSerializer.errors},status=400)
                            # supporterSerializer=SupporterSerializer(supporter,many=False)
                            # tempdata['supporter']=supporterSerializer.data
                        elif licence.role.pk==4:
                            print(profile.pk)
                            coach=Coach.objects.filter(profile_id=profile.pk).first()
                            #print(coach.profile.user.pk)
                            
                            print(request.data['coach'])
                            coachSerializer=CoachSerializer(coach,data=request.data['coach'],partial=True)
                            print('b')
                            if coachSerializer.is_valid():
                                print('c')
                                coachSerializer.save()
                                print('d')
                            else:
                                return JsonResponse({'message':coachSerializer.errors},status=400)
                            # coachSerializer=CoachSerializer(coach,many=False)
                            # tempdata['coach']=coachSerializer.data
            licenceSerializer=LicencesSerializer(licence,data=request.data['licence'],partial=True)
            if licenceSerializer.is_valid():
                licenceSerializer.save()
            else:
                return JsonResponse({'message':licenceSerializer.errors})
            # profileSerializer=ProfileSerializer(profile,data=request.data['profile'],partial=True)
            # if profileSerializer.is_valid():
            #     profileSerializer.save()
            # else:
            #     return JsonResponse({'message':profileSerializer.errors})
            return JsonResponse({'data':coachSerializer.data,
                                 'Licence':licenceSerializer.data,
                                 'profile':licenceSerializer.data
                                 })
            
            
    except Exception as e:
            return Response({'message':'There was a problem please try again later',
                             'error':str(e)
                             },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def licencelist_info(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':
            tempdata=[]
            licence = Licences.objects.all()
            if 'season' in request.data and request.data['season']!=None and request.data['season']!='': 
                licence=licence.filter(seasons=request.data['season'])    
            if 'state' in request.data and request.data['state']!=None and request.data['state']!='':
                licence=licence.filter(state=request.data['state']) 
            if 'role' in request.data and request.data['role']!=None and request.data['role']!='':
                licence=licence.filter(role=request.data['role'])    
            if 'user' in request.data and request.data['user']!=None and request.data['user']!='':
                licence=licence.filter(user=request.data['user'])
            if 'club' in request.data and request.data['club']!=None and request.data['club']!='':
                licence=licence.filter(club=request.data['club'])    

            licenceSerializer = LicencesSerializer(licence, many=True)
            for ls in licenceSerializer.data:
                tempdata.append({'licence':ls})
            # tempdata=licenceSerializer.data
            i=0
            for l in licence:
                if l.categorie!=None:
                    categorie = Categorie.objects.filter(id=l.categorie.pk).first()
                    ageSerializer = CategorieSerializer(categorie, many=False)
                    tempdata[i]['licence']['categorie']=categorie.categorie_age
                if l.seasons!=None:
                    season = Seasons.objects.filter(id=l.seasons.pk).first()
                    seasonSerializer = SeasonsSerializer(season, many=False)
                    tempdata[i]['licence']['seasons']=season.Seasons
                # ligue = Ligue.objects.filter(id=l.ligue.pk).first()
                # ligueSerializer =LigueSerializer(ligue, many=False)
                # tempdata[i]['ligue']=ligue.name
                if l.degree!=None:
                    degree = Degree.objects.filter(id=l.degree.pk).first()
                    degreeSerializer =DegreeSerializer(degree, many=False)
                    tempdata[i]['licence']['degree']=degree.Degree
                if l.discipline!=None:
                    discipline = Discipline.objects.filter(id=l.discipline.pk).first()
                    discSerializer =DisciplineSerializer(discipline, many=False)
                    tempdata[i]['licence']['discipline']=discipline.name
                if l.role!=None:
                    r = role.objects.filter(id=l.role.pk).first()
                    roleSerializer =RoleSerializer(r, many=False)
                    tempdata[i]['licence']['role']=r.roles
                if l.weight!=None:
                    weight = Weights.objects.filter(id=l.weight.pk).first()
                    weightSerializer =WeightSerializer(weight, many=False)
                    tempdata[i]['licence']['weight']=weight.masse_en_killograme
                if l.grade!=None:
                    grade = Grade.objects.filter(id=l.grade.pk).first()
                    gradeSerializer =GradeSerializer(grade, many=False)
                    tempdata[i]['licence']['grade']=grade.Grade
                if l.club!=None:
                    club = Club.objects.filter(id=l.club.pk).first()
                    clubSerializer =ClubSerializer(club, many=False)
                    tempdata[i]['licence']['club']=club.name
                if l.user!=None:
                    user = User.objects.filter(id=l.user.pk).first()
                    userserializer = UserSerializer(user, many=False)
                    # print(user.pk)
                    profile = Profile.objects.filter(user=user.pk).first()
                    profileSerializer =ProfileSerializer(profile, many=False)
                    if l.role!=None and profile!=None:
                        if l.role.pk==1:
                            arbitrator=Arbitrator.objects.filter(profile=profile.pk).first()
                            arbitratorSerializer=ArbitratorSerializer(arbitrator,many=False)
                            tempdata[i]['data']=arbitratorSerializer.data
                        elif l.role.pk==2:
                            athlete=Athlete.objects.filter(profile=profile.pk).first()
                            athleteSerializer=AthleteSerializer(athlete,many=False)
                            tempdata[i]['data']=athleteSerializer.data
                        elif l.role.pk==3:
                            supporter=Supporter.objects.filter(profile=profile.pk).first()
                            supporterSerializer=SupporterSerializer(supporter,many=False)
                            tempdata[i]['data']=supporterSerializer.data
                        elif l.role.pk==4:
                            coach=Coach.objects.filter(profile=profile.pk).first()
                            coachSerializer=CoachSerializer(coach,many=False)
                            tempdata[i]['data']=coachSerializer.data
                    

                    tempdata[i]['profile']=profileSerializer.data
                i=i+1
        return JsonResponse(tempdata,safe=False)
    except Exception as e:
            return Response({'message':'There was a problem please try again later',
                             'error':str(e)
                             },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def add_club(request):
    """
    Retrieve, update or delete a code Profile.
    """

    if request.method == 'POST':   
        try:
            print(request.data['user'])
            user=User(username=request.data['user']['username'])
            user.set_password(request.data['user']['password'])

            data={
                "username":user.username,
                "password":user.password
            }
            userSerializer=UserSerializer(data=data)
            if userSerializer.is_valid():
                userSerializer.save()
                
                tempProfile=request.data['profile']
                tempProfile['user']=userSerializer.data['id']
                profileSerializer=ProfileSerializer(data=tempProfile)
                
                if profileSerializer.is_valid():
                    profileSerializer.save()
                    tempClub=request.data['club']
                    tempClub['profile']=profileSerializer.data['id']
                    clubSerializer=ClubSerializer(data=tempClub)
            
                    if clubSerializer.is_valid():
                        clubSerializer.save()
                        return JsonResponse(clubSerializer.data,safe=False,status=201)
                    else:
                        return JsonResponse({"message":clubSerializer.errors},status=400)
                else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
            else:
                return JsonResponse({"message":userSerializer.errors},status=400)
        except Exception as e:
            return JsonResponse({
                "message":"There was a problem please try again later",
                "error":str(e)},status=500)
            
        
    

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def activate_season(request,pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'PUT':     
            seasons=Seasons.objects.all()
            # mySeasonSerializer=
            for s in seasons:
                if s.id==pk:
                    active={"activated":True}
                    
                    seasonSerializer=SeasonsSerializer(s,data=active,partial=True)
                    if seasonSerializer.is_valid():
                        print('aaaaa')
                        seasonSerializer.save()
                    else:
                        return JsonResponse({"message":seasonSerializer.errors},status=400)
                else:
                    active={"activated":False}
                    seasonSerializer=SeasonsSerializer(s,data=active,partial=True)
                    if seasonSerializer.is_valid():
                        print('bbbbb')
                        seasonSerializer.save()
                    else:
                        return JsonResponse({"message":seasonSerializer.errors},status=400)
        return JsonResponse({"activated":"The season was successfully activated"})
    except Exception as e:
            return JsonResponse({
                "message":"There was a problem please try again later",
                "error":str(e)},status=500)



@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def change_password(request,pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        user=User.objects.filter(id=pk).first()
        user.set_password( request.data['password'])
        data={"password":user.password}
        userSerializer=UserSerializer(user,data=data,partial=True)
        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse({"message":"Password was successfully changed"})
        else:
            return JsonResponse({"message":userSerializer.errors})
    except Exception as e:
            return JsonResponse({
                "message":"There was a problem please try again later",
                "error":str(e)},status=500)

        




@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def upload_photo(request):
    # data=request.data
    # print(request.FILES)
    try:
        data={}
        data['name']=request.FILES['url'].name
        extension=request.FILES['url'].name.split(".").pop()
        data['extension']=extension
        data['size']=request.FILES['url'].size
        data['url']=request.FILES['url']
        data['path']=request.data['path']
        data['season']=request.data['season']
        data['user']=request.data['user']
        imageSerializer=ImageSerializer(data=data)
        if imageSerializer.is_valid():
            imageSerializer.save()
            return JsonResponse(imageSerializer.data)
        else:
            return JsonResponse({"message":"Couldn't upload the image "+imageSerializer.errors})
    except Exception as e:
        return JsonResponse({"message":"There was a problem please try again",
                             "error": str(e)
                             })

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def active_season(request):
    try:
        season=Seasons.objects.filter(activated=True).first()
        seasonsSerializer =SeasonsSerializer(season)
        if seasonsSerializer.is_valid:
            return JsonResponse(seasonsSerializer.data)
        else:
            return JsonResponse({"message":seasonsSerializer.error})
    except Exception as e:
        return JsonResponse({"message":"There was a problem please try again",
                             "error": str(e)
                             })
    



@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def add_athlete(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'POST':   
            user=User()
            verifusername=''
            #print(request.data['user'])
            if 'username' in request.data['user'] and request.data['user']['username']!=None and request.data['user']['username']!='': 
                #user=User(username=request.data['user']['username'])
                user.username=request.data['user']['username']
                verifusername=user.username
            else:
                username=Username.objects.last()
                usernameNumber=int(username.created_username)
                usernameNumber=usernameNumber+1
                newusername=str(usernameNumber)
                usernameSerializer=UsernameSerializer(data={'created_username':newusername})
                if usernameSerializer.is_valid():
                    usernameSerializer.save()
                    verifusername=newusername
                    
                else:
                    return JsonResponse({"message":usernameSerializer.errors})
                print(username.created_username)
                #user.username=username.created_username
                #user=User(username=username.created_username)
            user.set_password(request.data['user']['password'])
            tempUser=request.data['user']
            tempUser['is_staff']=False
            tempUser['password']=user.password
            print(user.username)
            tempUser['username']=verifusername
            
            userSerializer=UserSerializer(data=tempUser)
            if userSerializer.is_valid():
                userSerializer.save()
                tempProfile=request.data['profile']
                tempProfile['user']=userSerializer.data['id']
                profileSerializer=ProfileSerializer(data=tempProfile)
                
                if profileSerializer.is_valid():
                    profileSerializer.save()
                    tempAthlete=request.data['athlete']
                    tempAthlete['profile']=profileSerializer.data['id']
                    athleteSerializer=AthleteSerializer(data=tempAthlete)
                
                    if athleteSerializer.is_valid():
                        athleteSerializer.save()
                        data={"user":userSerializer.data,
                            "profile":profileSerializer.data,
                            "athlete":athleteSerializer.data
                            }
                        return JsonResponse(data,safe=False,status=201)
                    else:
                        return JsonResponse({"message":athleteSerializer.errors},status=400)
                else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
            else:
                return JsonResponse({"message":userSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)



@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def add_coach(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'POST':   
            
            user=User(username=request.data['user']['username'])
            user.set_password(request.data['user']['password'])
            tempUser=request.data['user']
            tempUser['is_staff']=False
            tempUser['password']=user.password
            
            userSerializer=UserSerializer(data=tempUser)
            if userSerializer.is_valid():
                userSerializer.save()
                tempProfile=request.data['profile']
                tempProfile['user']=userSerializer.data['id']
                profileSerializer=ProfileSerializer(data=tempProfile)
                
                if profileSerializer.is_valid():
                    profileSerializer.save()
                    tempCoach=request.data['coach']
                    tempCoach['profile']=profileSerializer.data['id']
                    coachSerializer=CoachSerializer(data=tempCoach)
                
                    if coachSerializer.is_valid():
                        coachSerializer.save()
                        data={"user":userSerializer.data,
                            "profile":profileSerializer.data,
                            "coach":coachSerializer.data
                            }
                        return JsonResponse(data,safe=False,status=200)
                    else:
                        return JsonResponse({"message":coachSerializer.errors},status=400)
                else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
            else:
                return JsonResponse({"message":userSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
    
    
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def add_arbitrator(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'POST':   
            
            user=User(username=request.data['user']['username'])
            user.set_password(request.data['user']['password'])
            tempUser=request.data['user']
            tempUser['is_staff']=False
            tempUser['password']=user.password
            
            userSerializer=UserSerializer(data=tempUser)
            if userSerializer.is_valid():
                userSerializer.save()
                tempProfile=request.data['profile']
                tempProfile['user']=userSerializer.data['id']
                profileSerializer=ProfileSerializer(data=tempProfile)
                
                if profileSerializer.is_valid():
                    profileSerializer.save()
                    tempArbitrator=request.data['arbitrator']
                    tempArbitrator['profile']=profileSerializer.data['id']
                    arbitratorSerializer=ArbitratorSerializer(data=tempArbitrator)
                
                    if arbitratorSerializer.is_valid():
                        arbitratorSerializer.save()
                        data={"user":userSerializer.data,
                            "profile":profileSerializer.data,
                            "arbitrator":arbitratorSerializer.data
                            }
                        return JsonResponse(data,safe=False,status=200)
                    else:
                        return JsonResponse({"message":arbitratorSerializer.errors},status=400)
                else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
            else:
                return JsonResponse({"message":userSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
    
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def add_supporter(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'POST':   
            
            user=User(username=request.data['user']['username'])
            user.set_password(request.data['user']['password'])
            tempUser=request.data['user']
            tempUser['is_staff']=False
            tempUser['password']=user.password
            
            userSerializer=UserSerializer(data=tempUser)
            if userSerializer.is_valid():
                userSerializer.save()
                tempProfile=request.data['profile']
                tempProfile['user']=userSerializer.data['id']
                profileSerializer=ProfileSerializer(data=tempProfile)
                
                if profileSerializer.is_valid():
                    profileSerializer.save()
                    tempSupporter=request.data['supporter']
                    tempSupporter['profile']=profileSerializer.data['id']
                    supporterSerializer=SupporterSerializer(data=tempSupporter)
                
                    if supporterSerializer.is_valid():
                        supporterSerializer.save()
                        
                        return JsonResponse(supporterSerializer.data,safe=False,status=200)
                    else:
                        return JsonResponse({"message":supporterSerializer.errors},status=400)
                else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
            else:
                return JsonResponse({"message":userSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def filter_images(request):
    # if request.data['season']!=None and request.data['season']!=None:
    try:
        if 'path' in request.data and request.data['path']!=None and request.data['path']!='':
            if 'season' in request.data and request.data['season']!=None and request.data['season']!='':    
                
                if 'user' in request.data and request.data['user']!=None and request.data['user']!='':
                    print('a')
                    images=Image.objects.filter(path=request.data['path']).filter(url__contains=request.data['season']).filter(url__contains=request.data['user'])
                    imageSerializer=ImageSerializer(images,many=True)
                else:
                    print('b')
                    images=Image.objects.filter(path=request.data['path']).filter(url__contains=request.data['season'])
                    imageSerializer=ImageSerializer(images,many=True)
                    
            else:
                if 'user' in request.data and request.data['user']!=None and request.data['user']!='':
                    print('c')
                    images=Image.objects.filter(path=request.data['path']).filter(url__contains=request.data['user'])
                    imageSerializer=ImageSerializer(images,many=True)
                else:
                    print('d')
                    images=Image.objects.filter(path=request.data['path'])
                    imageSerializer=ImageSerializer(images,many=True)
                
        else:
            if 'season' in request.data and request.data['season']!=None and request.data['season']!='':    
                
                if 'user' in request.data and request.data['user']!=None and request.data['user']!='':
                    print('e')
                    images=Image.objects.filter(url__contains=request.data['season']).filter(url__contains=request.data['user'])
                    imageSerializer=ImageSerializer(images,many=True)
                else:
                    print('f')
                    images=Image.objects.filter(url__contains=request.data['season'])
                    imageSerializer=ImageSerializer(images,many=True)
            else:   
                if 'user' in request.data and request.data['user']!=None and request.data['user']!='':
                    print('g')
                    images=Image.objects.filter(url__contains=request.data['user'])
                    imageSerializer=ImageSerializer(images,many=True)
                else:
                    print('h')
                    images=Image.objects.all()
                    imageSerializer=ImageSerializer(images,many=True)
        return JsonResponse(imageSerializer.data,safe=False)
    except Exception as e:
        return JsonResponse({'message':'There was a problem please try again later',
                             'error':str(e)
                             })


    
    
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def athletelist_info(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':   
            athletes=Athlete.objects.all()
            athleteSerializer=AthleteSerializer(athletes,many=True)
            tempdata=[]
            if athleteSerializer.is_valid:
                
                for a in athleteSerializer.data:
                    if a['profile']!=None:
                        tempd={}
                        profile=Profile.objects.filter(id=a['profile']).first()
                        profileSerializer=ProfileSerializer(profile,many=False)
                        if profileSerializer.is_valid:
                            
                            if profileSerializer.data['user']!=None:
                                user=User.objects.filter(id=profile.user.id).first()
                                userSerializer=UserSerializer(user,many=False)
                                if userSerializer.is_valid:
                                    if a['grade_id']!=None:
                                        grade=Grade.objects.filter(id=a['grade_id']).first()
                                        gradeSerializer=GradeSerializer(grade,many=False)
                                    if a['id_degree']!=None:
                                        degree=Degree.objects.filter(id=a['id_degree']).first()
                                        degreeSerializer=DegreeSerializer(degree,many=False)
                                    #     print(degree.Degree)
                                    if a['category_id']!=None:
                                        category=Categorie.objects.filter(id=a['category_id']).first()
                                        categorySerializer=CategorieSerializer(category,many=False)
                                    if a['weights']!=None:
                                        weights=Weights.objects.filter(id=a['weights']).first()
                                        weightsSerializer=WeightSerializer(weights,many=False)
                                    if a['club']!=None:
                                        club=Club.objects.filter(id=a['club']).first()
                                        clubSerializer=ClubSerializer(club,many=False)
                                    
                                    
                                    tempd['profile']=profileSerializer.data
                                    tempd['user']=userSerializer.data
                                    tempd['athlete']=a
                                    if a['grade_id']!=None:
                                        tempd['athlete']['grade_id']=str(grade)
                                    if a['id_degree']!=None:
                                        tempd['athlete']['id_degree']=str(degree)
                                    tempd['athlete']['category_id']=str(category)
                                    tempd['athlete']['weights']=str(weights)
                                    tempd['athlete']['club']=str(club)
                                    tempdata.append(tempd)
                                    
                                else:
                                    return JsonResponse({"message":userSerializer.errors},status=400)    
                        else:
                            return JsonResponse({"message":profileSerializer.errors},status=400)
                return JsonResponse(tempdata,safe=False)
            
            else:
                return JsonResponse({"message":athleteSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
        
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def coachlist_info(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':   
            coaches=Coach.objects.all()
            coachSerializer=CoachSerializer(coaches,many=True)
            tempdata=[]
            if coachSerializer.is_valid:
                
                for c in coachSerializer.data:
                    if c['profile']!=None:
                        tempd={}
                        profile=Profile.objects.filter(id=c['profile']).first()
                        profileSerializer=ProfileSerializer(profile,many=False)
                        if profileSerializer.is_valid:
                            
                            if profileSerializer.data['user']!=None:
                                user=User.objects.filter(id=profile.user.id).first()
                                userSerializer=UserSerializer(user,many=False)
                                if userSerializer.is_valid:
                                    
                                    if c['grade']!=None:
                                        grade=Grade.objects.filter(id=c['grade']).first()
                                        gradeSerializer=GradeSerializer(grade,many=False)
                                    if c['degree']!=None:
                                        degree=Degree.objects.filter(id=c['degree']).first()
                                        degreeSerializer=DegreeSerializer(degree,many=False)
                                    #     print(degree.Degree)
                                    if c['category']!=None:
                                        category=Categorie.objects.filter(id=c['category']).first()
                                        categorySerializer=CategorieSerializer(category,many=False)
                                    if c['weights']!=None:
                                        weights=Weights.objects.filter(id=c['weights']).first()
                                        weightsSerializer=WeightSerializer(weights,many=False)
                                    if c['club']!=None:
                                        club=Club.objects.filter(id=c['club']).first()
                                        clubSerializer=ClubSerializer(club,many=False)
                                    
                                    
                                    tempd['profile']=profileSerializer.data
                                    tempd['user']=userSerializer.data
                                    tempd['coach']=c
                                    if c['grade']!=None:
                                        tempd['coach']['grade']=str(grade)
                                    if c['degree']!=None:
                                        tempd['coach']['degree']=str(degree)
                                    tempd['coach']['category']=str(category)
                                    tempd['coach']['weights']=str(weights)
                                    tempd['coach']['club']=str(club)
                                    tempdata.append(tempd)
                                    
                                else:
                                    return JsonResponse({"message":userSerializer.errors},status=400)    
                        else:
                            return JsonResponse({"message":profileSerializer.errors},status=400)
                return JsonResponse(tempdata,safe=False)
            
            else:
                return JsonResponse({"message":athleteSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
        
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def arbitratorlist_info(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':   
            arbitrators=Arbitrator.objects.all()
            arbitratorSerializer=ArbitratorSerializer(arbitrators,many=True)
            tempdata=[]
            if arbitratorSerializer.is_valid:
                
                for a in arbitratorSerializer.data:
                    if a['profile']!=None:
                        tempd={}
                        profile=Profile.objects.filter(id=a['profile']).first()
                        profileSerializer=ProfileSerializer(profile,many=False)
                        if profileSerializer.is_valid:
                            
                            if profileSerializer.data['user']!=None:
                                user=User.objects.filter(id=profile.user.id).first()
                                userSerializer=UserSerializer(user,many=False)
                                if userSerializer.is_valid:
                                    
                                    tempd['profile']=profileSerializer.data
                                    tempd['user']=userSerializer.data
                                    tempd['arbitrator']=a
                                    tempdata.append(tempd)
                                    
                                else:
                                    return JsonResponse({"message":userSerializer.errors},status=400)    
                        else:
                            return JsonResponse({"message":profileSerializer.errors},status=400)
                return JsonResponse(tempdata,safe=False)
            
            else:
                return JsonResponse({"message":athleteSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def supporterlist_info(request):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':   
            supporters=Supporter.objects.all()
            supporterSerializer=SupporterSerializer(supporters,many=True)
            tempdata=[]
            if supporterSerializer.is_valid:
                
                for s in supporterSerializer.data:
                    if s['profile']!=None:
                        tempd={}
                        profile=Profile.objects.filter(id=s['profile']).first()
                        profileSerializer=ProfileSerializer(profile,many=False)
                        if profileSerializer.is_valid:
                            
                            if profileSerializer.data['user']!=None:
                                user=User.objects.filter(id=profile.user.id).first()
                                userSerializer=UserSerializer(user,many=False)
                                if userSerializer.is_valid:
                                    
                                    tempd['profile']=profileSerializer.data
                                    tempd['user']=userSerializer.data
                                    tempd['arbitrator']=s
                                    tempdata.append(tempd)
                                    
                                else:
                                    return JsonResponse({"message":userSerializer.errors},status=400)    
                        else:
                            return JsonResponse({"message":profileSerializer.errors},status=400)
                return JsonResponse(tempdata,safe=False)
            
            else:
                return JsonResponse({"message":athleteSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def activate_user(request,pk):
    try:
        user=User.objects.filter(id=pk).first()
        tempdata={}
        if user.is_active==True:
            tempdata={'is_active':False}       
            userSerializer=UserSerializer(user,data=tempdata,partial=True)        
            if userSerializer.is_valid():            
                userSerializer.save() 
            else:
                return JsonResponse({'message':userSerializer.errors},status=400)      
        else:    
            tempdata={'is_active':True}
            userSerializer=UserSerializer(user,data=tempdata,partial=True)
            if userSerializer.is_valid():
                userSerializer.save()
            else:
                return JsonResponse({'message':userSerializer.errors},status=400)          
        return JsonResponse(userSerializer.data)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
    

    
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def edit_athlete_profile(request,pk):
    try:
        tempdata={}
        if 'athlete' in request.data:
            athlete=Athlete.objects.filter(id=pk).first()
            athleteSerializer=AthleteSerializer(athlete,data=request.data['athlete'],partial=True)
            if athleteSerializer.is_valid():
                athleteSerializer.save()
                tempdata['athlete']=athleteSerializer.data
            else:
                return JsonResponse({'message':athleteSerializer.errors},status=400)
        
        if 'profile' in request.data:
            profile=Profile.objects.filter(id=athlete.profile.pk).first()
            profileSerializer=ProfileSerializer(profile,data=request.data['profile'],partial=True)
            if profileSerializer.is_valid():
                profileSerializer.save()
                tempdata['profile']=profileSerializer.data
            else:
                return JsonResponse({'message':profileSerializer.errors},status=400)
        return JsonResponse(tempdata,safe=False)
    except Exception as e:
         return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
            
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def edit_coach_profile(request,pk):
    try:
        tempdata={}
        if 'coach' in request.data:
            coach=Coach.objects.filter(id=pk).first()
            coachSerializer=CoachSerializer(coach,data=request.data['coach'],partial=True)
            if coachSerializer.is_valid():
                coachSerializer.save()
                tempdata['coach']=coachSerializer.data
            else:
                return JsonResponse({'message':coachSerializer.errors},status=400)
        
        if 'profile' in request.data:
            profile=Profile.objects.filter(id=coach.profile.pk).first()
            profileSerializer=ProfileSerializer(profile,data=request.data['profile'],partial=True)
            if profileSerializer.is_valid():
                profileSerializer.save()
                tempdata['profile']=profileSerializer.data
            else:
                return JsonResponse({'message':profileSerializer.errors},status=400)
        return JsonResponse(tempdata,safe=False)
    except Exception as e:
         return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
            
            
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def edit_arbitrator_profile(request,pk):
    try:
        tempdata={}
        if 'arbitrator' in request.data:
            arbitrator=Arbitrator.objects.filter(id=pk).first()
            arbitratorSerializer=ArbitratorSerializer(arbitrator,data=request.data['arbitrator'],partial=True)
            if arbitratorSerializer.is_valid():
                arbitratorSerializer.save()
                tempdata['arbitrator']=arbitratorSerializer.data
            else:
                return JsonResponse({'message':arbitratorSerializer.errors},status=400)
        
        if 'profile' in request.data:
            profile=Profile.objects.filter(id=arbitrator.profile.pk).first()
            profileSerializer=ProfileSerializer(profile,data=request.data['profile'],partial=True)
            if profileSerializer.is_valid():
                profileSerializer.save()
                tempdata['profile']=profileSerializer.data
            else:
                return JsonResponse({'message':profileSerializer.errors},status=400)
        return JsonResponse(tempdata,safe=False)
    except Exception as e:
         return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
            
            
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def edit_supporter_profile(request,pk):
    try:
        tempdata={}
        if 'supporter' in request.data:
            supporter=Supporter.objects.filter(id=pk).first()
            supporterSerializer=SupporterSerializer(supporter,data=request.data['supporter'],partial=True)
            if supporterSerializer.is_valid():
                supporterSerializer.save()
                tempdata['supporter']=supporterSerializer.data
            else:
                return JsonResponse({'message':supporterSerializer.errors},status=400)
        
        if 'profile' in request.data:
            profile=Profile.objects.filter(id=supporter.profile.pk).first()
            profileSerializer=ProfileSerializer(profile,data=request.data['profile'],partial=True)
            if profileSerializer.is_valid():
                profileSerializer.save()
                tempdata['profile']=profileSerializer.data
            else:
                return JsonResponse({'message':profileSerializer.errors},status=400)
        return JsonResponse(tempdata,safe=False)
    except Exception as e:
         return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
         
         


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def stats(request):
    try:
        tempdata={}
        
        athletes=Athlete.objects.all().__len__()
        tempdata['athletes']=athletes
        coaches=Coach.objects.all().__len__()
        tempdata['coaches']=coaches
        arbitrators=Arbitrator.objects.all().__len__()
        tempdata['arbitrators']=arbitrators
        supporters=Supporter.objects.all().__len__()
        tempdata['supporters']=supporters
        clubs=Club.objects.all().__len__()
        tempdata['clubs']=clubs
        licences=Licences.objects.all().__len__()
        activeLicences=Licences.objects.filter(state="Activee").__len__()
        pendingLicences=Licences.objects.filter(state="En Attente").__len__()
        expiredLicences=Licences.objects.filter(state="Expiree").__len__()
        tempdata['active_licences']=activeLicences
        tempdata['pending_licences']=pendingLicences
        tempdata['expired_licences']=expiredLicences
        athletesLicences=Licences.objects.filter(role=2).__len__()   
        tempAthletes={}
        tempAthletes['total']=athletesLicences  
        activeAthletesLicences=Licences.objects.filter(role=2).filter(state='Activee').__len__()
        pendingAthletesLicences=Licences.objects.filter(role=2).filter(state='En Attente').__len__()
        expiredAthletesLicences=Licences.objects.filter(role=2).filter(state='Expiree').__len__()
        tempAthletes['active']=activeAthletesLicences
        tempAthletes['pending']=pendingAthletesLicences
        tempAthletes['expired']=expiredAthletesLicences
        tempdata['athletes_licences']=tempAthletes
        
        coachesLicences=Licences.objects.filter(role=4).__len__()   
        tempCoaches={}
        tempCoaches['total']=coachesLicences  
        activeCoachesLicences=Licences.objects.filter(role=4).filter(state='Activee').__len__()
        pendingCoachesLicences=Licences.objects.filter(role=4).filter(state='En Attente').__len__()
        expiredCoachesLicences=Licences.objects.filter(role=4).filter(state='Expiree').__len__()
        tempCoaches['active']=activeCoachesLicences
        tempCoaches['pending']=pendingCoachesLicences
        tempCoaches['expired']=expiredCoachesLicences
        tempdata['coaches licences']=tempCoaches
        
        arbitratorsLicences=Licences.objects.filter(role=1).__len__()   
        tempArbitrators={}
        tempArbitrators['total']=arbitratorsLicences  
        activeArbitratorsLicences=Licences.objects.filter(role=1).filter(state='Activee').__len__()
        pendingArbitratorsLicences=Licences.objects.filter(role=1).filter(state='En Attente').__len__()
        expiredArbitratorsLicences=Licences.objects.filter(role=1).filter(state='Expiree').__len__()
        tempArbitrators['active']=activeArbitratorsLicences
        tempArbitrators['pending']=pendingArbitratorsLicences
        tempArbitrators['expired']=expiredArbitratorsLicences
        tempdata['arbitrators licences']=tempArbitrators
        
        supportersLicences=Licences.objects.filter(role=3).__len__()   
        tempSupporters={}
        tempSupporters['total']=supportersLicences  
        activeSupportersLicences=Licences.objects.filter(role=3).filter(state='Activee').__len__()
        pendingSupportersLicences=Licences.objects.filter(role=3).filter(state='En Attente').__len__()
        expiredSupportersLicences=Licences.objects.filter(role=3).filter(state='Expiree').__len__()
        tempSupporters['active']=activeSupportersLicences
        tempSupporters['pending']=pendingSupportersLicences
        tempSupporters['expired']=expiredSupportersLicences
        tempdata['supporters licences']=tempSupporters
        
        tempUsers={}
        users=User.objects.all().__len__()
        activeUsers=User.objects.filter(is_active=True).__len__()
        inactiveUsers=User.objects.filter(is_active=False).__len__()
        staffUsers=User.objects.filter(is_staff=True).__len__()
        admins=User.objects.filter(is_superuser=True).__len__()
        tempUsers['total']=users
        tempUsers['active']=activeUsers
        tempUsers['inactive']=inactiveUsers
        tempUsers['staff']=staffUsers
        tempUsers['admins']=admins
        tempdata['users']=tempUsers
        
        return JsonResponse(tempdata)
    except Exception as e:
         return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
         
         



@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def forced_delete(request,pk):
    try:
        user=User.objects.filter(id=pk).first()
        profile=Profile.objects.filter(user=pk).first()
        if profile.role.pk==1:
            arbitrator=Arbitrator.objects.filter(profile=profile.pk)
            licences=Licences.objects.filter(user=pk)
            for licence in licences:
                licence.delete()
            arbitrator.delete()
        profile.delete()
        user.delete()
        return JsonResponse({'message':'All data assosciated with the provided user has been deleted'},status=204)
    except Exception as e:
         return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
         
         
         
         
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def athlete_info(request,pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':   
            tempd={}
            athletes=Athlete.objects.filter(id=pk).first()
            athleteSerializer=AthleteSerializer(athletes,many=False)
            
            if athleteSerializer.is_valid:
                
                if athleteSerializer.data['profile']!=None:
                    
                    profile=Profile.objects.filter(id=athleteSerializer.data['profile']).first()
                    profileSerializer=ProfileSerializer(profile,many=False)
                    if profileSerializer.is_valid:
                            
                        if profileSerializer.data['user']!=None:
                            user=User.objects.filter(id=profile.user.id).first()
                            userSerializer=UserSerializer(user,many=False)
                            if userSerializer.is_valid:
                                    
                                tempd['profile']=profileSerializer.data
                                tempd['user']=userSerializer.data
                                tempd['athlete']=athleteSerializer.data
                                
                                    
                            else:
                                return JsonResponse({"message":userSerializer.errors},status=400)    
                    else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
                return JsonResponse(tempd,safe=False)
            
            else:
                return JsonResponse({"message":athleteSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
        
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def coach_info(request,pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':   
            tempd={}
            coaches=Coach.objects.filter(id=pk).first()
            coachSerializer=CoachSerializer(coaches,many=False)
            
            if coachSerializer.is_valid:
                
                
                if coachSerializer.data['profile']!=None:
                    
                    profile=Profile.objects.filter(id=coachSerializer.data['profile']).first()
                    profileSerializer=ProfileSerializer(profile,many=False)
                    if profileSerializer.is_valid:
                        
                        if profileSerializer.data['user']!=None:
                            user=User.objects.filter(id=profile.user.id).first()
                            userSerializer=UserSerializer(user,many=False)
                            if userSerializer.is_valid:
                                    
                                tempd['profile']=profileSerializer.data
                                tempd['user']=userSerializer.data
                                tempd['coach']=coachSerializer.data
                                
                                    
                            else:
                                return JsonResponse({"message":userSerializer.errors},status=400)    
                    else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
                return JsonResponse(tempd,safe=False)
            
            else:
                return JsonResponse({"message":athleteSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)
        
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def arbitrator_info(request,pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':   
            tempd={}
            arbitrators=Arbitrator.objects.filter(id=pk).first()
            arbitratorSerializer=ArbitratorSerializer(arbitrators,many=False)
            
            if arbitratorSerializer.is_valid:
                
                
                if arbitratorSerializer.data['profile']!=None:
                    
                    profile=Profile.objects.filter(id=arbitratorSerializer.data['profile']).first()
                    profileSerializer=ProfileSerializer(profile,many=False)
                    if profileSerializer.is_valid:
                            
                        if profileSerializer.data['user']!=None:
                            user=User.objects.filter(id=profile.user.id).first()
                            userSerializer=UserSerializer(user,many=False)
                            if userSerializer.is_valid:
                                    
                                tempd['profile']=profileSerializer.data
                                tempd['user']=userSerializer.data
                                tempd['arbitrator']=arbitratorSerializer.data
                                
                                    
                            else:
                                return JsonResponse({"message":userSerializer.errors},status=400)    
                    else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
                return JsonResponse(tempd,safe=False)
            
            else:
                return JsonResponse({"message":athleteSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
def supporter_info(request,pk):
    """
    Retrieve, update or delete a code Profile.
    """
    try:
        if request.method == 'GET':  
            tempd={} 
            supporters=Supporter.objects.filter(id=pk).first()
            supporterSerializer=SupporterSerializer(supporters,many=False)
            if supporterSerializer.is_valid:
                
                
                if supporterSerializer.data['profile']!=None:
                    
                    profile=Profile.objects.filter(id=supporterSerializer.data['profile']).first()
                    profileSerializer=ProfileSerializer(profile,many=False)
                    if profileSerializer.is_valid:
                            
                        if profileSerializer.data['user']!=None:
                            user=User.objects.filter(id=profile.user.id).first()
                            userSerializer=UserSerializer(user,many=False)
                            if userSerializer.is_valid:
                                    
                                tempd['profile']=profileSerializer.data
                                tempd['user']=userSerializer.data
                                tempd['arbitrator']=supporterSerializer.data
                                    
                                    
                            else:
                                return JsonResponse({"message":userSerializer.errors},status=400)    
                    else:
                        return JsonResponse({"message":profileSerializer.errors},status=400)
                return JsonResponse(tempd,safe=False)
            
            else:
                return JsonResponse({"message":athleteSerializer.errors},status=400)
    except Exception as e:
        return JsonResponse({
            "message":"There was a problem please try again later",
            "error":str(e)},status=500)

         
         
         

         
