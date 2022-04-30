def get_part_list(a_vec):
    fragment = 100
    
    output = [a_vec[i:i + fragment] for i in range(0, len(a_vec), fragment)]

    for i in range(0, len(output)):
        output[i] = ([x.strip() for x in output[i]])

    return output

def create_sql_file(a_vec, file_name):
    str_sql = ''
    
    for item in a_vec:                        
        str_sql += f"UPDATE `suscripcion` SET `estado` = false WHERE `Id` IN ({','.join(item)})\n"

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(str_sql)

with open("data_ids.csv", "r", encoding="utf-8") as f:
    content_file = f.readlines()

fragments_list = get_part_list(content_file)

create_sql_file(fragments_list, 'archivo_partes.sql')