from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created_date', 'published_date', )

    class Media:
        js = (
            '/static/js/tinymce/tinymce.min.js',
            '/static/js/tinymce/config.js',
            '/static/js/tinymce/plugins/image/plugin.min.js',
            '/static/js/syntaxhighlighter/scripts/shBrushJScript.js',
            '/static/js/syntaxhighlighter/scripts/shBrushBash.js',
            '/static/js/syntaxhighlighter/scripts/shBrushPhp.js',
            '/static/js/syntaxhighlighter/scripts/shBrushJava.js',
            '/static/js/syntaxhighlighter/scripts/shBrushSql.js',
            '/static/js/syntaxhighlighter/scripts/shBrushXml.js',
            '/static/js/syntaxhighlighter/scripts/shBrushPython.js',
            '/static/js/syntaxhighlighter/scripts/shBrushCss.js',
            '/static/js/syntaxhighlighter/scripts/shBrushCpp.js',
        )

admin.site.register(Article,ArticleAdmin)
