from rest_framework import serializers
from .models import Cpu, Memory, Mobo, Storage, Videocard

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = [
            'id',
            'manufacturer',
            'model_name',
            'part_number',
            'price',
            'series',
            'family',
            'cores',
            'threads',
            'base_clock',
            'boost_clock',
        ]

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = [
            'id',
            'manufacturer',
            'model_name',
            'part_number',
            'price',
            'speed',
            'frequency',
            'memory_type',
            'isdual',
            'ram',
            'cas_latency',
            'isecc',
        ]

class MoboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobo
        fields = [
            'id',
            'manufacturer',
            'model_name',
            'part_number',
            'price',
            'socket',
            'chipset',
            'form_factor',
            'ram_slots',
            'max_ram',
            'sata',
            'm2',
            'pcie',
        ]
    
class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'id',
            'manufacturer',
            'model_name',
            'part_number',
            'price',
            'capacity',
            'cache',
            'interface',
        ]

class VideocardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videocard
        fields = [
            'id',
            'manufacturer',
            'model_name', 
            'part_number',
            'price',
            'chipset',
            'vram',
            'base_clock',
            'boost_clock',
        ]