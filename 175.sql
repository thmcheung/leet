select firstName as "firstName", lastName as "lastName", city, state
from Person left join Address
on Person.personID = Address.personID