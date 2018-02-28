# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-28 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_auto_20180226_squashed_0006_auto_20180227_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('external_id', models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('name', models.TextField(max_length=255)),
                ('organization_type', models.TextField(max_length=255)),
                ('usage_year', models.PositiveIntegerField(blank=True, null=True)),
                ('usd_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('original_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('original_currency', models.CharField(choices=[('AED', 'aed'), ('AFN', 'afn'), ('ALL', 'all'), ('AMD', 'amd'), ('ANG', 'ang'), ('AOA', 'aoa'), ('ARS', 'ars'), ('AUD', 'aud'), ('AWG', 'awg'), ('AZN', 'azn'), ('BAM', 'bam'), ('BBD', 'bbd'), ('BDT', 'bdt'), ('BGN', 'bgn'), ('BHD', 'bhd'), ('BIF', 'bif'), ('BMD', 'bmd'), ('BND', 'bnd'), ('BOB', 'bob'), ('BRL', 'brl'), ('BSD', 'bsd'), ('BTN', 'btn'), ('BWP', 'bwp'), ('BYN', 'byn'), ('BZD', 'bzd'), ('CAD', 'cad'), ('CDF', 'cdf'), ('CHF', 'chf'), ('CLP', 'clp'), ('CNY', 'cny'), ('COP', 'cop'), ('CRC', 'crc'), ('CUC', 'cuc'), ('CUP', 'cup'), ('CVE', 'cve'), ('CZK', 'czk'), ('DJF', 'djf'), ('DKK', 'dkk'), ('DOP', 'dop'), ('DZD', 'dzd'), ('EGP', 'egp'), ('ERN', 'ern'), ('ETB', 'etb'), ('EUR', '€'), ('FJD', 'fjd'), ('FKP', 'fkp'), ('GBP', 'gbp'), ('GEL', 'gel'), ('GGP', 'ggp'), ('GHS', 'ghs'), ('GIP', 'gip'), ('GMD', 'gmd'), ('GNF', 'gnf'), ('GTQ', 'gtq'), ('GYD', 'gyd'), ('HKD', 'hkd'), ('HNL', 'hnl'), ('HRK', 'hrk'), ('HTG', 'htg'), ('HUF', 'huf'), ('IDR', 'idr'), ('ILS', 'ils'), ('IMP', 'imp'), ('INR', 'inr'), ('IQD', 'iqd'), ('IRR', 'irr'), ('ISK', 'isk'), ('JEP', 'jep'), ('JMD', 'jmd'), ('JOD', 'jod'), ('JPY', 'jpy'), ('KES', 'kes'), ('KGS', 'kgs'), ('KHR', 'khr'), ('KMF', 'kmf'), ('KPW', 'kpw'), ('KRW', 'krw'), ('KWD', 'kwd'), ('KYD', 'kyd'), ('KZT', 'kzt'), ('LAK', 'lak'), ('LBP', 'lbp'), ('LKR', 'lkr'), ('LRD', 'lrd'), ('LSL', 'lsl'), ('LYD', 'lyd'), ('MAD', 'mad'), ('MDL', 'mdl'), ('MGA', 'mga'), ('MKD', 'mkd'), ('MMK', 'mmk'), ('MNT', 'mnt'), ('MOP', 'mop'), ('MRO', 'mro'), ('MUR', 'mur'), ('MVR', 'mvr'), ('MWK', 'mwk'), ('MXN', 'mxn'), ('MYR', 'myr'), ('MZN', 'mzn'), ('NAD', 'nad'), ('NGN', 'ngn'), ('NIO', 'nio'), ('NOK', 'nok'), ('NPR', 'npr'), ('NZD', 'nzd'), ('OMR', 'omr'), ('PAB', 'pab'), ('PEN', 'pen'), ('PGK', 'pgk'), ('PHP', 'php'), ('PKR', 'pkr'), ('PLN', 'pln'), ('PYG', 'pyg'), ('QAR', 'qar'), ('RON', 'ron'), ('RSD', 'rsd'), ('RUB', 'rub'), ('RWF', 'rwf'), ('SAR', 'sar'), ('SBD', 'sbd'), ('SCR', 'scr'), ('SDG', 'sdg'), ('SEK', 'sek'), ('SGD', 'sgd'), ('SHP', 'shp'), ('SLL', 'sll'), ('SOS', 'sos'), ('SPL', 'spl'), ('SRD', 'srd'), ('STD', 'std'), ('SVC', 'svc'), ('SYP', 'syp'), ('SZL', 'szl'), ('THB', 'thb'), ('TJS', 'tjs'), ('TMT', 'tmt'), ('TND', 'tnd'), ('TOP', 'top'), ('TRY', 'try'), ('TTD', 'ttd'), ('TVD', 'tvd'), ('TWD', 'twd'), ('TZS', 'tzs'), ('UAH', 'uah'), ('UGX', 'ugx'), ('USD', '$'), ('UYU', 'uyu'), ('UZS', 'uzs'), ('VEF', 'vef'), ('VND', 'vnd'), ('VUV', 'vuv'), ('WST', 'wst'), ('XAF', 'xaf'), ('XCD', 'xcd'), ('XDR', 'xdr'), ('XOF', 'xof'), ('XPF', 'xpf'), ('YER', 'yer'), ('YER1', 'yer1'), ('ZAR', 'zar'), ('ZMW', 'zmw'), ('ZWD', 'zwd'), ('ZWL', 'zwl')], default='USD', max_length=16)),
                ('exchange_rate', models.DecimalField(decimal_places=3, default=1, max_digits=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='external_source',
            field=models.TextField(blank=True, choices=[('RPM', 'RPM')], null=True),
        ),
        migrations.AddField(
            model_name='partnerproject',
            name='code',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='partnerproject',
            name='external_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partnerproject',
            name='external_id',
            field=models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='partner',
            unique_together=set([('external_id', 'external_source'), ('title', 'vendor_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='partnerproject',
            unique_together=set([('external_id', 'external_source')]),
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='partner_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funding_sources', to='partner.PartnerProject'),
        ),
    ]
