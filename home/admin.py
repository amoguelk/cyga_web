from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from .models import Announcement, Content

#######################################
#############Announcement##############
#######################################


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at", "archived"]
    list_filter = ["archived"]
    actions = ["archive_announcement", "unarchive_announcement"]

    @admin.action(description="Archivar anuncios seleccionados")
    def archive_announcement(self, request, queryset):
        updated = queryset.update(archived=True)
        self.message_user(
            request,
            ngettext(
                "%d anuncio fue archivado",
                "%d anuncios fueron archivados",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Desarchivar anuncios seleccionados")
    def unarchive_announcement(self, request, queryset):
        updated = queryset.update(archived=False)
        self.message_user(
            request,
            ngettext(
                "%d anuncio fue desarchivado",
                "%d anuncios fueron desarchivados",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


admin.site.register(Announcement, AnnouncementAdmin)

#######################################
################Content################
#######################################


class ContentAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "archived"]
    list_filter = ["type", "archived"]
    actions = ["archive_content", "unarchive_content"]

    @admin.action(description="Archivar contenido seleccionado")
    def archive_content(self, request, queryset):
        updated = queryset.update(archived=True)
        self.message_user(
            request,
            ngettext(
                "%d contenido fue archivado",
                "%d contenidos fueron archivados",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Desarchivar contenido seleccionado")
    def unarchive_content(self, request, queryset):
        updated = queryset.update(archived=False)
        self.message_user(
            request,
            ngettext(
                "%d contenido fue desarchivado",
                "%d contenidos fueron desarchivados",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


admin.site.register(Content, ContentAdmin)
