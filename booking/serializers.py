from rest_framework import serializers
from .models import *
from flights.models import Flight,Airline#,FlightSeatClass
from flights.models import *
from theaccount.models import User


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = '__all__'
        
        
class BookingSerializer10(serializers.ModelSerializer):  #get all 
    class Meta:
        model = Booking
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields =['user','Passenger','outbound_flight','return_flight','trip_type','passenger_class']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  
        
        
class FlightSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['airportDeparture','airportArrival']

class BookingSerializer1(serializers.ModelSerializer):
    outbound_flight = FlightSerializer1()

    class Meta:
        model = Booking
        fields = ['user', 'Passenger', 'outbound_flight', 'return_flight', 'trip_type', 'passenger_class','total_cost','booking_date','id']        
        
class AirlineSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['airline_name']

class FlightSerializer2(serializers.ModelSerializer):
    airline = AirlineSerializer2()  # تضمين معلومات الشركة الجوية

    class Meta:
        model = Flight
        fields = ['airportDeparture', 'airportArrival','airline']  # تضمين معلومات الشركة الجوية

class BookingSerializer2(serializers.ModelSerializer):
    outbound_flight = FlightSerializer2()

    class Meta:
        model = Booking
        fields = ['user', 'Passenger', 'outbound_flight', 'return_flight', 'trip_type', 'passenger_class', 'total_cost', 'booking_date','id']
        
        
############my Booking         
class FlightSerializer3(serializers.ModelSerializer):
    airline_name = serializers.CharField(source='Airplane.airline.airline_name')

    class Meta:
        model = Flight
        fields = ['airportDeparture', 'airportArrival', 'airline_name']

class BookingSerializer3(serializers.ModelSerializer):
    outbound_flight = FlightSerializer3()

    class Meta:
        model = Booking
        fields = ['user', 'Passenger', 'outbound_flight', 'return_flight', 'trip_type', 'passenger_class', 'total_cost', 'booking_date','status','id']


'''
class PushNotificationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotificationToken
        fields = '__all__'
'''
'''
    def validate(self, data):
     outbound_flight = data.get('outbound_flight')
     return_flight = data.get('return_flight')

     if outbound_flight == return_flight:
        raise serializers.ValidationError("Outbound and return flights cannot be the same")

     passengers_data = data.get('passengers', [])
     passenger_names = [passenger.get('name') for passenger in passengers_data]
     if len(passenger_names) != len(set(passenger_names)):
        raise serializers.ValidationError("Passenger names must be unique within a booking")

     passport_numbers = [passenger.get('passport_number') for passenger in passengers_data]
     if len(passport_numbers) != len(set(passport_numbers)):
        raise serializers.ValidationError("Passport numbers must be unique within a booking")
    # if not outbound_flight.flightseatclass_set.filter(id=seat_class_id).exists():
     #       raise serializers.ValidationError("Selected seat class is not available for the outbound flight")

     return data
'''


          
class AgencyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyPolicy
        fields = ['id', 'policy_type', 'percentage', 'duration', 'points', 'points_offers', 'conditions']      







####################### profile Tickets 

class AirplaneSerializerT(serializers.ModelSerializer):
    airline_name = serializers.CharField(source='airline.airline_name', read_only=True)
    
    class Meta:
        model = Airplane
        fields = ['airline_name']

class FlightSerializerT(serializers.ModelSerializer):
    Airplane = AirplaneSerializerT()
    class Meta:
        model = Flight
        fields = ['departure_date', 'departure_city','destination_city', 'airportDeparture', 'airportArrival', 'Airplane','duration']
class PassengerSerializerT(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'passport_number']

class BookingSerializerT(serializers.ModelSerializer):
    Passenger = PassengerSerializerT()
    outbound_flight = FlightSerializerT()
    return_flight = FlightSerializerT()
    
    class Meta:
        model = Booking
        fields = ['id', 'outbound_flight', 'return_flight','Passenger','passenger_class', 'trip_type', 'status', 'total_cost', 'creation_time']


 
############## pravetoffers 
class PriavateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyPolicy
        fields = ['conditions']

class PriavateSerializer1(serializers.ModelSerializer):
   # agency_policy = PriavateSerializer()

    class Meta:
        model = User
        fields = ['pointBalance']

 ########
class PriavateSerializer2(serializers.ModelSerializer):
    class Meta:
        model = AgencyPolicy
        fields = ['conditions']
        
class PrivateSerializer2(serializers.ModelSerializer):
    agency_policy = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['pointBalance', 'agency_policy']

    def get_agency_policy(self, obj):
        try:
            return PriavateSerializer2(obj.agencypolicy).data
        except AgencyPolicy.DoesNotExist:
            return None                


################3
#booking_details

class FlightSerializer100(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['airportDeparture', 'airportArrival','departure_date','duration']

class PassengerSerializer100(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name','gender','passport_number']

class BookingSerializer100(serializers.ModelSerializer):
    Passenger = PassengerSerializer100()
    outbound_flight = FlightSerializer100()
    return_flight = FlightSerializer100()

    class Meta:
        model = Booking
        fields = ['id','outbound_flight', 'return_flight', 'Passenger', 'total_cost']
