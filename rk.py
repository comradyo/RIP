# -*- coding: utf-8 -*-
from operator import itemgetter
 
class OpSys:
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class Comp:
    def __init__(self, id, brand, opSys_id):
        self.id = id
        self.brand = brand
        self.opSys_id = opSys_id
 
class CompOpSys:
    def __init__(self, id, comp_id, opSys_id):
        self.id = id
        self.comp_id = comp_id
        self.opSys_id = opSys_id
 
def main():
    opSyss = [
        OpSys(1, 'Windows'),
        OpSys(2, 'Linux'),
        OpSys(3, 'MacOS'),
        OpSys(4, 'TempleOS')
    ]

    comps = [
        Comp(1, 'Asus', 2),
        Comp(2, 'Asus', 2),
        Comp(3, 'Acer', 4),
        Comp(4, 'Dell', 2),
        Comp(5, 'Acer', 3),
        Comp(6, 'Msi', 4),
        Comp(7, 'HP', 1),
        Comp(8, 'Apple', 3),
    ]

    comps_opSyss = [
        CompOpSys(1, 1, 1),
        CompOpSys(2, 1, 4),
        CompOpSys(3, 2, 2),
        CompOpSys(4, 3, 1),
        CompOpSys(5, 2, 4),
        CompOpSys(6, 3, 4),
        CompOpSys(7, 1, 2),
        CompOpSys(8, 2, 4),
        CompOpSys(9, 5, 3),
        CompOpSys(10, 5, 1)
    ]

    one_to_many_b1 = [(op_sys.name, comp.brand) 
        for op_sys in opSyss
        for comp in comps
        if comp.opSys_id==op_sys.id]
 
    print('\n\nЗадание Б1')
    res_b1 = sorted(one_to_many_b1, key=itemgetter(0))
    print(res_b1)

    one_to_many_b2 = [(op_sys.name, 
            len(
                list(
                    filter(lambda x: x.opSys_id == op_sys.id, comps)
                    )
                ))
            for op_sys in opSyss]

    print('\n\nЗадание Б2')
    res_b2 = sorted(one_to_many_b2, key=itemgetter(1))
    print(res_b2)

    many_to_many_b3 = {comp.brand: [op_sys.name for op_sys in opSyss
            if op_sys.id in
                [c_os.opSys_id for c_os in comps_opSyss if c_os.comp_id == comp.id]]
            for comp in comps if str(comp.brand).startswith('A')}

    print('\n\nЗадание Б3')
    print(many_to_many_b3)
    print('\n\n')
 
if __name__ == '__main__':
    main()
