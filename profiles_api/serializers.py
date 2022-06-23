from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        """meta class"""
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class StudentSerializer(serializers.ModelSerializer):
    """Serializes Student items"""

    class Meta:
        model = models.Student
        fields = (
        'st_ID', 'st_name', 'st_family_name', 'st_course', 'st_undergraduate', 'st_year', 'st_age', 'st_birthdate',
        'st_contact_number', 'st_email')
        extra_kwargs = {'st_email': {'read_only': True}}


class BookSerializer(serializers.ModelSerializer):
    """Serializes Book items"""

    class Meta:
        models = models.Book
        fields = ('id', 'book_title', 'book_edition', 'book_author', 'book_publisher', 'book_copies')

    def validate(self, data):
        if data['book_copies'] < 0:
            raise serializers.ValidationError("Book's quantity cannot be negative!")
        elif data['book_copies'] < 4:
            raise serializers.ValidationError("The book cannot be further borrowed! There are not enough copies left")
        return data


class UsersSerializer(serializers.ModelSerializer):
    """Serializes Users items"""

    class Meta:
        models = models.Users
        fields = ('staff_ID', 'staff_name', 'staff_family_name', 'staff_contact', 'staff_email', 'staff_type')
        extra_kwargs = {'staff_ID': {'read_only': True}, 'staff_email': {'read_only': True}}


class BookTypeSerializer(serializers.ModelSerializer):
    """Serializes BookType items"""

    class Meta:
        models = models.BookType
        fields = ('book_ID', 'book_type')
        extra_kwargs = {'book_type': {'read_only': True}}


class BorrowersSerializer(serializers.ModelSerializer):
    """Serializes Borrowers items"""

    class Meta:
        models = models.Borrowers
        fields = ('book_ID', 'borrow_title', 'st_ID', 'release_date', 'return_date')
        extra_kwargs = {'borrow_title': {'read_only': True}, 'release_date': {'read_only': True}}

    def valid_date(self, data):
        if data['return_date'] < 0:
            raise serializers.ValidationError('The return date cannot be earlier than release date!')
        elif data['return_date'] > 45:
            raise serializers.ValidationError('The return date is too late!')
        return data
