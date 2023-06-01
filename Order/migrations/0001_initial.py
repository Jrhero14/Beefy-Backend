# Generated by Django 4.2.1 on 2023-06-01 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_PEMBAYARAN', models.IntegerField()),
                ('ID_PEMBELI', models.IntegerField()),
                ('ID_TOKO', models.IntegerField()),
                ('ID_BARANG', models.IntegerField()),
                ('catatan', models.CharField(max_length=255)),
                ('alamat_pengiriman', models.TextField()),
                ('metode_pembayaran', models.CharField(max_length=10)),
                ('tanggal_order', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Menunggu', 'Menunggu Diterima Seller'), ('Diproses', 'Diproses oleh kurir'), ('Selesai', 'Pesanan Selesai')], default='Menunggu', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bukti_bayar', models.CharField(max_length=255)),
                ('rekening', models.CharField(max_length=15)),
                ('total_harga', models.FloatField()),
                ('biaya_pengiriman', models.FloatField()),
                ('kode_unik', models.IntegerField()),
                ('status', models.CharField(choices=[('M', 'Menunggu'), ('T', 'Dibayar')], default='Menunggu', max_length=1)),
            ],
        ),
    ]