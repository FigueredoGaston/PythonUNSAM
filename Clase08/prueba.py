 ''' df_tipas_parques = df_parques[cols_sel_p].copy()
    df_tipas_veredas = df_veredas[cols_sel_v].copy()
    df_tipas_veredas.rename(columns={'altura_arbol':'altura_tot',
                                    'diametro_altura_pecho':'diametro',
                                    'nombre_cientifico':'nombre_cie'})
     df_tipas_parques.assign(ambiente = 'parque')
    df_tipas_veredas.assign(ambiente = 'vereda')
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques]) '''
    #df_tipas.boxplot('diametro', by = 'nombre_cie')