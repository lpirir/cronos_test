def get_half_list(a_vec):
    half = len(a_vec) // 2    
    return a_vec[:half], a_vec[half:]

def create_sql_file(a_vec, file_name):
    str_sql = ''
    
    for item in a_vec:                
        str_sql += f"UPDATE `suscripcion` SET `estado` = false WHERE `Id` = '{item.strip()}'\n"

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(str_sql)

with open("data_ids.csv", "r", encoding="utf-8") as f:
    content_file = f.readlines()

part_1, part_2 = get_half_list(content_file)

create_sql_file(part_1, 'archivo1.sql')
create_sql_file(part_2, 'archivo2.sql')