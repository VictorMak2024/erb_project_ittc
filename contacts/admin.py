from django.contrib import admin, messages
# from django.urls import path
# from django.shortcuts import redirect
from crud import export_all_data, import_all_data, clear_database
from .models import Activity_Contact, Course_Contact, Product_Contact, TakeOrder

from django.contrib import admin, messages
from crud import export_data, import_data

class CustomAdmin(admin.ModelAdmin):
    # Add custom actions
    actions = ['export_all_data_action', 'import_all_data_action', 'clear_database_action']
    def export_all_data_action(self, request, queryset):
        """Export all data to JSON files"""
        export_all_data()
        self.message_user(request, "All data exported successfully!", level=messages.SUCCESS)

    export_all_data_action.short_description = "Export All Data"

    def import_all_data_action(self, request, queryset):
        """Import all data from JSON files"""
        import_all_data()
        self.message_user(request, "All data imported successfully!", level=messages.SUCCESS)

    import_all_data_action.short_description = "Import All Data"

    def clear_database_action(self, request, queryset):
        """Clear all data from the database"""
        clear_database()
        self.message_user(request, "Database cleared successfully!", level=messages.WARNING)

    clear_database_action.short_description = "Clear Database"

# Add custom actions
    actions = ['export_data_action', 'import_data_action']


    def export_data_action(self, request, queryset):
        """Export data for the current model to a JSON file"""
        app_label = self.model._meta.app_label  # Get the app label dynamically
        model_name = self.model._meta.model_name  # Get the model name dynamically
        output_file = f"DATABASE/JSON/{model_name}.json"  # Define the output file path

        # Call the export_data function
        try:
            export_data(app_label, model_name, output_file)
            messages.success(request, f"Data exported successfully to {output_file}!")
        except Exception as e:
            messages.error(request, f"Error exporting data: {str(e)}")

    export_data_action.short_description = "Export Data"

    def import_data_action(self, request, queryset):
        """Import data for the current model from a JSON file"""
        app_label = self.model._meta.app_label  # Get the app label dynamically
        model_name = self.model._meta.model_name  # Get the model name dynamically
        input_file = f"DATABASE/JSON/{model_name}.json"  # Define the input file path

        # Call the import_data function
        try:
            success = import_data(input_file)
            if success:
                self.message_user(request, f"Data imported successfully from {input_file}!", level=messages.SUCCESS)
            else:
                self.message_user(request, f"Failed to import data from {input_file}.", level=messages.ERROR)
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    import_data_action.short_description = "Import Data"
    # def export_data_action(self, request, queryset):
    #     """Export data to a file"""
    #     export_data()
    #     self.message_user(request, "Data exported successfully!", level=messages.SUCCESS)

    # export_data_action.short_description = "Export Data"

    # def import_data_action(self, request, queryset):
    #     """Import data from a file"""
    #     import_data()
    #     self.message_user(request, "Data imported successfully!", level=messages.SUCCESS)

    # import_data_action.short_description = "Import Data"

class Activity_ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'contact_date', 'activity_id', 'is_paid')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'activity_id')
    list_per_page = 25

admin.site.register(Activity_Contact, Activity_ContactAdmin)

class Course_ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'contact_date', 'course_id', 'is_paid')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'course_id')
    list_per_page = 25

admin.site.register(Course_Contact, Course_ContactAdmin)

class Product_ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'name', 'email', 'phone', 'contact_date', 'product_id')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'product_id')
    list_per_page = 25

admin.site.register(Product_Contact, Product_ContactAdmin)

class TakeOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price','onOrderQty', 'contact_date', 'ordered','user_id')
    list_display_links = ('id', 'product')
    #search_fields = ('product')
    list_per_page = 25

admin.site.register(TakeOrder, TakeOrderAdmin)
