from sys import flags
from django.contrib.auth.models import User
from rest_framework import serializers, validators

from finalback.models import  (
    Arbitrator,
    Username,
    Image,
    ArchivedLicences,
    Coach,
    Athlete,
    Competition,
    Bracket,
    Match,
    Result,
    Club,
    Profile,
    role,
    Supporter,
    Categorie,
    Weights,
    Seasons,
    Grade,
    Licences,
    Degree,
    Discipline,
    Ligue

    
)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        extra_kwargs = {
            "role": {
                "required": False,
               
                },

            "password": {"write_only": True},
            "username": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "هذا الأسم مستخدم الرجاء إدخال أسم جديد"
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            # role=validated_data["role"],
            # email=validated_data["email"],
            # first_name=validated_data["first_name"],
            # last_name=validated_data["last_name"]
        )
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = '__all__'
        
        
class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'


class ArbitratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbitrator
        fields = '__all__'
        
class LigueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligue
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class SupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supporter
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weights
        fields = '__all__'


class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class LicencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licences
        fields = '__all__'
        
class ArchivedLicencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivedLicences
        fields = '__all__'
        
class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'
        
class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'
        
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        
class BracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bracket
        fields = '__all__'
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        
        
class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Username
        fields = '__all__'
        
        
