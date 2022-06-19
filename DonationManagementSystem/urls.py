"""DonationManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from donation.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('all_logins', all_logins, name='all_logins'),
    path('donor_login', donor_login, name='donor_login'),
    path('volunteer_login', volunteer_login, name='volunteer_login'),
    path('admin_login', admin_login, name='admin_login'),
    path('donor_reg', donor_reg, name='donor_reg'),
    path('donor_home', donor_home, name='donor_home'),
    path('volunteer_home', volunteer_home, name='volunteer_home'),
    path('logout/', Logout, name='logout'),
    path('donate_now', donate_now, name='donate_now'),
    path('donation_history', donation_history, name='donation_history'),
    path('admin_home', admin_home, name='admin_home'),
    path('pending_donation', pending_donation, name='pending_donation'),
    path('pending_donationdetail/<int:pid>', pending_donationdetail, name='pending_donationdetail'),
    path('accepted_donation', accepted_donation, name='accepted_donation'),
path('rejected_donation', rejected_donation, name='rejected_donation'),
    path('add_area', add_area, name='add_area'),
    path('manage_area', manage_area, name='manage_area'),
    path('edit_area/<int:pid>', edit_area, name='edit_area'),
    path('delete_area/<int:pid>', delete_area, name='delete_area'),
    path('manage_donor', manage_donor, name='manage_donor'),
    path('view_donordetail/<int:pid>', view_donordetail, name='view_donordetail'),
    path('delete_donor/<int:pid>', delete_donor, name='delete_donor'),
    path('volunteer_reg', volunteer_reg, name='volunteer_reg'),
    path('new_volunteer', new_volunteer, name='new_volunteer'),
    path('view_volunteerdetail/<int:pid>', view_volunteerdetail, name='view_volunteerdetail'),
    path('accepted_volunteer', accepted_volunteer, name='accepted_volunteer'),
    path('rejected_volunteer', rejected_volunteer, name='rejected_volunteer'),
    path('all_volunteer', all_volunteer, name='all_volunteer'),
    path('delete_volunteer/<int:pid>', delete_volunteer, name='delete_volunteer'),
path('accepted_donationdetail/<int:pid>', accepted_donationdetail, name='accepted_donationdetail'),
path('rejected_donationdetail/<int:pid>', rejected_donationdetail, name='rejected_donationdetail'),
path('deliver_donationdetail/<int:pid>', deliver_donationdetail, name='deliver_donationdetail'),
path('all_deliver_donationdetail', all_deliver_donationdetail, name='all_deliver_donationdetail'),
path('all_undeliver_donationdetail', all_undeliver_donationdetail, name='all_undeliver_donationdetail'),
path('see_deliver_donationdetail<int:pid>', see_deliver_donationdetail, name='see_deliver_donationdetail'),
path('volunteer_profile/<int:pid>', volunteer_profile, name='volunteer_profile'),
path('donor_profile/<int:pid>', donor_profile, name='donor_profile'),
path('edit_volunteer_profile/<int:pid>', edit_volunteer_profile, name='edit_volunteer_profile'),
path('donor_rejected_donationdetail/<int:pid>', donor_rejected_donationdetail, name='donor_rejected_donationdetail'),
path('donor_pending_donationdetail/<int:pid>', donor_pending_donationdetail, name='donor_pending_donationdetail'),
path('donor_delivered_donationdetail/<int:pid>', donor_delivered_donationdetail, name='donor_delivered_donationdetail'),
path('donor_accepted_donationdetail/<int:pid>', donor_accepted_donationdetail, name='donor_accepted_donationdetail'),
path('donor_donationNotReceived_donationdetail/<int:pid>', donor_donationNotReceived_donationdetail, name='donor_donationNotReceived_donationdetail'),
path('our_gallery', our_gallery, name='our_gallery'),
path('more_details/<int:pid>', more_details, name='more_details'),
path('about_us', about_us, name='about_us'),
path('contact_us', contact_us, name='contact_us'),
path('orphanages', orphanages, name='orphanages'),
path('add_orphanages', add_orphanages, name='add_orphanages'),
path('orphanage_more_detail', orphanage_more_detail, name='orphanage_more_detail'),
    path('collection_req', collection_req, name='collection_req'),
    path('donationcollection_detail/<int:pid>', donationcollection_detail, name='donationcollection_detail'),
    path('donationrec_volunteer', donationrec_volunteer, name='donationrec_volunteer'),
    path('donationrec_detail/<int:pid>', donationrec_detail, name='donationrec_detail'),
path('all_donation', all_donation, name='all_donation'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
