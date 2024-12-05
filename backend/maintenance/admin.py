from django.contrib import admin
from .models import Mechanic, BreakdownLog, Machine


class MachineAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('category', 'type', 'brand', 'model_number', 'serial_no', 'status', 'location', 'purchase_date', 'last_breakdown_start')
    
    # Fields that will be used for filtering the machines in the list view
    list_filter = ('status', 'category', 'brand', 'location', 'floor_no', 'line_no')
    
    # Fields to search in the list view
    search_fields = ('category', 'type', 'brand', 'model_number', 'serial_no', 'location')
    
    # Fields that should be displayed in the detail view (edit form)
    fields = ('category', 'type', 'brand', 'model_number', 'serial_no', 'supplier', 'purchase_date', 'location', 'floor_no', 'line_no', 'status', 'last_breakdown_start')
    
    # Customize the ordering of machines in the list view
    ordering = ('-purchase_date',)  # Display the most recently purchased machines first
    
    # Fields that are readonly in the edit view (form view)
    readonly_fields = ('serial_no',)  # If you don't want the serial number to be editable
    
    # Enable the ability to add machines in the list view (useful for bulk actions)
    actions = ['mark_active', 'mark_inactive', 'mark_maintenance', 'mark_broken']

    def mark_active(self, request, queryset):
        queryset.update(status='active')
    mark_active.short_description = "Mark selected machines as Active"

    def mark_inactive(self, request, queryset):
        queryset.update(status='inactive')
    mark_inactive.short_description = "Mark selected machines as Inactive"

    def mark_maintenance(self, request, queryset):
        queryset.update(status='maintenance')
    mark_maintenance.short_description = "Mark selected machines as Under Maintenance"

    def mark_broken(self, request, queryset):
        queryset.update(status='broken')
    mark_broken.short_description = "Mark selected machines as Broken"

class BreakdownLogAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('machine', 'mechanic', 'operator', 'problem_category', 'breakdown_start', 'lost_time', 'comments')

    # Add search functionality
    search_fields = ('machine__category', 'mechanic__name', 'operator__name', 'problem_category')

    # Add filter options
    list_filter = ('machine', 'mechanic', 'operator', 'problem_category', 'breakdown_start')

    # Add ordering for the list view
    ordering = ('-breakdown_start',)

    # Add date hierarchy for better navigation of records
    date_hierarchy = 'breakdown_start'

    # Organize fields into sections
    fieldsets = (
        (None, {
            'fields': ('machine', 'mechanic', 'operator', 'problem_category', 'breakdown_start')
        }),
        ('Breakdown Details', {
            'fields': ('lost_time', 'comments')
        })
    )

# Register the BreakdownLog model with its custom BreakdownLogAdmin
admin.site.register(BreakdownLog, BreakdownLogAdmin)

# Register the admin class with the Machine model
admin.site.register(Machine, MachineAdmin)

# admin.site.register(Mechanic)
# admin.site.register(Machine)