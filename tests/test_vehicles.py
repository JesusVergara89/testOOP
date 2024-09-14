import unittest
from src.vehicles import Vehicle, Car, Motorbike

class TestVehicle(unittest.TestCase):
    
    def test_vehicle_abstract_class(self):
        with self.assertRaises(TypeError):
            Vehicle("Generic", "Model")
    
    def test_car(self):
        car = Car("Toyota", "Corolla", 4)
        self.assertEqual(car.get_brand(), 3)
        self.assertEqual(car.get_model(), "Corolla")
        self.assertEqual(car.start_engine(), "Toyota Corolla engine started with a key.")

    def test_motorbike(self):
        """Verifica el comportamiento de la clase Motorbike"""
        bike = Motorbike("Yamaha", "MT-07", 689)
        self.assertEqual(bike.get_brand(), "Yamaha")
        self.assertEqual(bike.get_model(), "MT-07")
        self.assertEqual(bike.start_engine(), "Yamaha MT-07 engine started with a button.")

if __name__ == '__main__':
    unittest.main()
