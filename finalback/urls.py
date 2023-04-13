from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    #just for testing the token
    path('user/', views.get_user),
    path('image/', views.ImageList.as_view()),
    path('image/<int:pk>/', views.ImageDetail.as_view()),
    path('discipline/', views.DisciplineList.as_view()),
    path('discipline/<int:pk>/', views.DisciplineDetail.as_view()),
    path('role/', views.RoleList.as_view()),
    path('role/<int:pk>/', views.RoleDetail.as_view()),
    path('arbitrator/', views.ArbitratorList.as_view()),
    path('arbitrator/<int:pk>/', views.ArbitratorDetail.as_view()),
    path('coach/', views.CoachList.as_view()),
    path('coach/<int:pk>/', views.CoachDetail.as_view()),
    path('competition/', views.CompetitionList.as_view()),
    path('competition/<int:pk>/', views.CompetitionDetail.as_view()),
    path('match/', views.MatchList.as_view()),
    path('match/<int:pk>/', views.MatchDetail.as_view()),  
    path('result/', views.ResultList.as_view()),
    path('result/<int:pk>/', views.ResultDetail.as_view()),
    path('bracket/', views.BracketList.as_view()),
    path('bracket/<int:pk>/', views.BracketDetail.as_view()),    
    path('archived/', views.ArchivedList.as_view()),
    path('archived/<int:pk>/', views.ArchivedDetail.as_view()),
    path('athlete/', views.AthleteList.as_view()),
    path('athlete/<int:pk>/', views.AthleteDetail.as_view()),
    path('club/', views.ClubList.as_view()),
    path('club/<int:pk>/', views.ClubDetail.as_view()),
    path('ligue/', views.LigueList.as_view()),
    path('ligue/<int:pk>/', views.LigueDetail.as_view()),
    path('profile/', views.ProfileList.as_view()),
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    path('supporter/', views.SupporterList.as_view()),
    path('supporter/<int:pk>/', views.SupporterDetail.as_view()),
    path('export/csv/', views.export_users_csv),
    path('export/xls/', views.export_users_xls),
    #path('alluser/', views.showthis),
    path('allusers/', views.UserList.as_view()),
    path('allusers/<int:pk>/', views.UserDetail.as_view()),
    path('categorie/', views.CategorieList.as_view()),
    path('categorie/<int:pk>/', views.CategorieDetail.as_view()),
    path('licences/', views.LicencesList.as_view()),
    path('licences/<str:pk>/', views.LicencesDetail.as_view()),
    path('grade/', views.GradeList.as_view()),
    path('grade/<int:pk>/', views.GradeDetail.as_view()),
    path('seasons/', views.SeasonsList.as_view()),
    path('seasons/<int:pk>/', views.SeasonsDetail.as_view()),
    path('weights/', views.WeightsList.as_view()),
    path('weights/<int:pk>/', views.WeightsDetail.as_view()),
    path('degree/', views.DegreeList.as_view()),
    path('degree/<int:pk>/', views.DegreeDetail.as_view()),
    path('username/', views.UsernameList.as_view()),
    path('username/<int:pk>/', views.UsernameDetail.as_view()),
    # path('pro/', views.pro_list),
    path('prolist/',views.pro_list),
    path('pro/<int:pk>/',views.user_info),
    path('user_licences/<int:pk>/',views.user_licences),
    path('role_licences/<int:pk>/',views.role_licences),
    path('licence_info/<str:pk>/',views.licence_info),
    path('licencelist_info/',views.licencelist_info),
    path('add_club/',views.add_club),

    path('parameters/',views.parameters),
    path('verifyLicence/<str:pk>/',views.verify_licence),
    path('validateLicence/<str:pk>/',views.validate_licence),

    path('club_licences/<int:pk>/',views.club_licences),
    path('add_licence/',views.add_licence),
    path('renew_licence/<str:pk>/',views.renew_licence),
    path('comp_info/<int:pk>/',views.comp_info),
    path('create_manager/',views.create_manager),
    path('activate_season/<int:pk>/',views.activate_season),
    path('change_password/<int:pk>/',views.change_password),
    path('upload_photo/',views.upload_photo),
    path('active_season/',views.active_season),
    path('add_athlete/',views.add_athlete),
    path('add_coach/',views.add_coach),
    path('add_arbitrator/',views.add_arbitrator),
    path('filter_images/',views.filter_images),
    path('athletelist_info/',views.athletelist_info),
    path('coachlist_info/',views.coachlist_info),
    path('arbitratorlist_info/',views.arbitratorlist_info),
    path('supporterlist_info/',views.supporterlist_info),
    path('activate_user/<int:pk>/',views.activate_user),
    path('edit_athlete_profile/<int:pk>/',views.edit_athlete_profile),
    path('edit_coach_profile/<int:pk>/',views.edit_coach_profile),
    path('edit_arbitrator_profile/<int:pk>/',views.edit_arbitrator_profile),
    path('edit_supporter_profile/<int:pk>/',views.edit_supporter_profile),
    path('stats/',views.stats),
    path('forced_delete/<int:pk>/',views.forced_delete),
    path('athlete_info/<int:pk>/',views.athlete_info),
    path('coach_info/<int:pk>/',views.coach_info),
    path('arbitrator_info/<int:pk>/',views.arbitrator_info),
    path('supporter_info/<int:pk>/',views.supporter_info),
    path('arbitrator_by_licence/<str:pk>/',views.arbitrator_by_licence),
    path('comp_arbitrator_list/',views.comp_arbitrator_list),
    path('participant_by_licence/<str:pk>/',views.participant_by_licence),

    path('comp_participants_list/',views.comp_participants_list),
    path('comp_list_info/',views.comp_list_info),
    path('add_matches/',views.addMatches),
    path('submit_result/<int:pk>/',views.submitResult),
    path('clubs_list/',views.clubsList),
    path('add_full_licence/',views.add_full_licence),
    path('edit_athlete_licence/',views.edit_athlete_licence)







    # path('data/',views.getmydata),





    


    # path('create_athlete/',views.create_athlete),

]