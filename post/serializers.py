from rest_framework import serializers
from post.models import *

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ["company_name","business_area"]


class JobPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPost
        fields = ["job_type","company","job_description","salary"]


class JobPostSkillSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostSkillSet
        fields = ["skill_set","job_post"]


