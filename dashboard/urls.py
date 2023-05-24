from django.urls import path, re_path
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings

from . import views, AirportsViews, projectsViews


app_name = 'dashboard' 
urlpatterns = [ 
    # Dashboard Bulletin 
    path('bulletin',views.BulletinHome,name='bulletin'),
    path('bulletinCreate',views.BulletinCreate,name='bulletinCreate'),    
    path('bulletinaknldg/<int:id>',views.Bulletin_Aknldg,name='bulletinaknldg'),    
    path('bulletincomment/<int:id>',views.Bulletin_Comment,name='bulletincomment'),
    # Airport Profile
    path('airports',AirportsViews.Airports,name='airports'),
    path('airportmap',AirportsViews.AirportMap,name='airportmap'),
    path('areaC1',AirportsViews.AreaCenter1,name='areaC1'),
    path('areaC2',AirportsViews.AreaCenter2,name='areaC2'),
    path('areaC3',AirportsViews.AreaCenter3,name='areaC3'),
    path('areaC4',AirportsViews.AreaCenter4,name='areaC4'),
    path('areaC5',AirportsViews.AreaCenter5,name='areaC5'),
    path('areaC6',AirportsViews.AreaCenter6,name='areaC6'),
    path('areaC7',AirportsViews.AreaCenter7,name='areaC7'),
    path('areaC8',AirportsViews.AreaCenter8,name='areaC8'),
    path('areaC9',AirportsViews.AreaCenter9,name='areaC9'),
    path('areaC10',AirportsViews.AreaCenter10,name='areaC10'),
    path('areaC11',AirportsViews.AreaCenter11,name='areaC11'),
    path('areaC12',AirportsViews.AreaCenter12,name='areaC12'),

    # Airport Projects
    path('caap_ap',projectsViews.index),    
    path('airportproject/<str:name>',projectsViews.Project), 
    path('view/<int:id>',projectsViews.viewProject),
    path('show/<int:id>',projectsViews.showView),
    path('',projectsViews.dashView),
    path('auth',projectsViews.login_view),   
    path('logout',projectsViews.logout_view),    
    
    path('info/', projectsViews.infoView),
    path('addnew',projectsViews.addnew),
    path('complete-projects',projectsViews.complete_projects),
    path('ongoing-projects',projectsViews.ongoing_projects),
    path('procurement-projects',projectsViews.procurement_projects),
    path('edit/<int:id>', projectsViews.edit),  
    path('project_update/<int:id>', projectsViews.update),  
    path('delete/<int:id>', projectsViews.destroy),  
    
    path('progress/', projectsViews.progress_view),

  
    # Media Url Pattern    
    re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], views.protected_serve, {'document_root': settings.MEDIA_ROOT}),
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
