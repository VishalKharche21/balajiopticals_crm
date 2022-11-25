
from django.urls import path,include
from opticalcrm import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.site.site_header = 'Shree Balaji Opticals CRM'                   
# admin.site.index_title = 'Features area'                 
# admin.site.site_title = 'HTML title from adminsitration'

urlpatterns = [
    path('',views.index),
    path('login',views.sbologin, name='login'),
    path("AfterLogin", views.AfterLogin,name='AfterLogin'),
    path("logout/",views.sbologout,name='logout'),
    path('Dashboard',views.fun, name='main'),
    

    # ===========invoice==========
    path('Dashboard/Invoice-Generate',views.invoice_generate, name='invoice-generate'),
    path('Dashboard/Invoice-ajax',views.invoice_ajax, name='invoice_ajax'),
    path('Dashboard/Invoice-getdata-ajax',views.invoice_product_ajax, name='invoice_product_ajax'),
    path('Dashboard/Invoice-getdatag-ajax',views.invoice_productg_ajax, name='invoice_productg_ajax'),
    path('Dashboard/Invoice-List',views.invoicelist, name='invoicelist'),
    path('Dashboard/getbillno',views.getbillno, name='getbillno'),
    path('Dashboard/Sales/Pending-Amount',views.pending_amount, name='pending_amount'),
    path('Dashboard/Sales/Pending-Order',views.pending_order, name='pending_order'),
    path('Dashboard/Sales/Update-Pending-Order/<int:id>',views.update_order, name='update_order'),
    path('Dashboard/Sales/Update-Pending-Order1/<int:id>',views.update_order1, name='update_order1'),
    path('Dashboard/Sales/Order-Completed-List',views.complete_order, name='complete_order'),
    path('Dashboard/Sales/Order-Deliver-Option/<int:id>',views.deliver_option, name='deliver_option'),
    path('Dashboard/Sales/Order-deliver_anyway/<int:id>',views.deliver_anyway, name='deliver_anyway'),
    path('Dashboard/Sales/Invoice-Print/<int:id>',views.download_invoice_view, name='download_invoice_view'),
    path('Dashboard/Sales/Invoice/',views.download_invoice_print, name='download_invoice_print'),

    # ===========customer===========
    path('addcustomer',views.add_customer, name='addcustomer'),
    path('Dashboard/Customer/Customer-List',views.customer_list, name='customer_list'),
    path('Dashboard/Customer/Customer-List/Customer-Details/<int:id>',views.customer_details_view, name='customer_details_view'),
    path('Dashboard/Customer/Customer-List/Customer-Update/<int:id>',views.customer_update, name='customer_update'),
    path('Dashboard/Customer/Add-Customer/',views.customer_add, name='customer_add'),

    # =============purchase==========
    path('Dashboard/Purchase/Add-Purchase/',views.purchase_add, name='purchase_add'),
    path('Dashboard/Purchase/Add-Supplier/',views.supplier_add, name='supplier_add'),
    path('Dashboard/Purchase/Supplier-List/',views.supplier_list, name='supplier_list'),
    path('Dashboard/Purchase/Supplier-Update/<int:id>',views.supplier_update, name='supplier_update'),

    # =============product===========
    path('Dashboard/Products/Frame/',views.frame_add, name='frame_add'),
    path('Dashboard/Products/Glasses/',views.glass_add, name='glass_add'),
    path('Dashboard/Products/Goggles/',views.goggles_add, name='goggles_add'),

    # ==============purchase===========
    path('autocomplete/', views.pautocomplete, name='autocomplete'),
    path('gautocomplete/', views.gautocomplete, name='gautocomplete'),
    path('ggautocomplete/', views.ggautocomplete, name='ggautocomplete'),
    path('purchase-data-get/', views.purchaseajax, name='purchaseajax'),
    path('purchase-glass-data-get/', views.purchasegajax, name='purchasegajax'),
    path('purchase-goggles-data-get/', views.purchaseggajax, name='purchaseggajax'),
    path('Dashboard/Purchase/Confirm-Barcode/', views.confirm_barcode, name='confirm_barcode'),
    path('Dashboard/Purchase/Confirm-Barcode/<int:id>', views.confirm_barcodeid, name='confirm_barcodeid'),
    path('Dashboard/Purchase/Purchase-History/', views.purchase_history, name='purchase_history'),

    # =============inventory============
    path('Dashboard/Inventory/', views.inventory_details, name='inventory_details'),

    # =============prescription=============
    path('Dashboard/Prescription/Add-Prescription', views.prescription_add, name='prescription_add'),
    path('Dashboard/Prescription/prescription-ajax', views.prescription_ajax, name='prescription_ajax'),
    path('Dashboard/Prescription/prescription-Data', views.prescription_data, name='prescription_data'),
    path('Dashboard/Prescription/prescription-Print/<int:id>', views.download_pdf_view, name='prescription_pdf'),
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)