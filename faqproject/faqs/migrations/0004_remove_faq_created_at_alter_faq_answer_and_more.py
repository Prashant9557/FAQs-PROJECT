# Generated by Django 5.1.5 on 2025-02-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0003_faq_answer_ar_faq_answer_as_faq_answer_bh_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ar',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_as',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_bh',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_bn',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_de',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_es',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_fa',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_fr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_gu',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_he',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_hi',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ind',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_it',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ja',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_kn',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ko',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ma',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ml',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_mr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ne',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_nl',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_or',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_pa',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_pl',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_pt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_sd',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_sn',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ta',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_te',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_th',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_tr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ur',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_vi',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_zh',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_as',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_bh',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_bn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_fa',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_gu',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_he',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_hi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ind',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_it',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_kn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ko',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ma',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ml',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_mr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ne',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_nl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_or',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_pa',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_pl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_sd',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_sn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ta',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_te',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_th',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_tr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_vi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_zh',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
