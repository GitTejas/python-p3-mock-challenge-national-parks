class NationalPark:

    def __init__(self, name):
        self._name = name
        self._trips = []
        self._visitors = []
            
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
           name

    def trips(self):
        return self._trips
        
    def visitors(self):
        return list({trip.visitor for trip in self._trips})
        # return list(set([trip.visitor for trip in self._trips]))
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        if not self._trips:
            return None
        visitor_counts = {}
        for trip in self._trips:
            visitor_counts[trip.visitor] = visitor_counts.get(trip.visitor, 0) + 1
        return max(visitor_counts, key=visitor_counts.get)

class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        national_park._trips.append(self)
        national_park._visitors.append(self)
        visitor._trips.append(self)
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if type(value) == str and 1 <= len(value) >= 7:
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if type(value) == str and 1 <= len(value) >= 7:
            self._end_date = value
    
class Visitor:

    def __init__(self, name):
        self._name = name
        self._trips = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <=15:
            self._name = name
        
    def trips(self):
        return self._trips
    
    def national_parks(self):
        return list({trip.national_park for trip in self._trips})
        # return list(set([trip.national_park for trip in self._trips]))
    
    def total_visits_at_park(self, park):
        return sum(1 for trip in self._trips if trip.national_park == park)