######################################## TFA ########################################

# import pandas as pd
#
# df = pd.read_csv(
#     "sfda_TFA.csv",
#     encoding="utf-8-sig",
#     encoding_errors="replace",
#     on_bad_lines="skip",
#     engine="python",
# )
#
# before = len(df)
# df = df[df['source_type'] == 'TFA']
# df = df.drop_duplicates()
# df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
#
# print(f"Dropped {before - len(df)} bad/duplicate rows")
# print(f"Final rows    : {len(df):,}")
# print(f"Columns ({len(df.columns)}): {df.columns.tolist()}")
# print(f"\nArabic check  : {df['manufacture_CountryAr'].head(3).tolist()}")
#
# df.to_csv("sfda_TFA_final.csv", index=False, encoding="utf-8-sig")
# print("\nSaved → sfda_TFA_final.csv")

######################################## GHTF ########################################

# df = pd.read_csv(
#     "sfda_GHTF.csv",
#     encoding="utf-8-sig",
#     encoding_errors="replace",
#     on_bad_lines="skip",
#     engine="python",
# )
#
# before = len(df)
# df = df[df['source_type'] == 'GHTF']
# df = df.drop_duplicates()
# df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
#
# print(f"Dropped {before - len(df)} bad/duplicate rows")
# print(f"Final rows    : {len(df):,}")
# print(f"Columns ({len(df.columns)}): {df.columns.tolist()}")
# print(f"\nArabic check  : {df['manufacture_CountryAr'].head(3).tolist()}")
#
# df.to_csv("sfda_GHTF_final.csv", index=False, encoding="utf-8-sig")
# print("\nSaved → sfda_GHTF_final.csv")



######################################## LOWRISK ########################################

#
# df = pd.read_csv(
#     "sfda_Lowrisk.csv",
#     encoding="utf-8-sig",
#     encoding_errors="replace",
#     on_bad_lines="skip",
#     engine="python",
# )
#
# before = len(df)
# df = df[df['source_type'] == 'Lowrisk']
# df = df.drop_duplicates()
# df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
#
# print(f"Dropped {before - len(df)} bad/duplicate rows")
# print(f"Final rows    : {len(df):,}")
# print(f"Columns ({len(df.columns)}): {df.columns.tolist()}")
# print(f"\nArabic check  : {df['manufactureCountryAR'].head(3).tolist()}")
#
# df.to_csv("sfda_Lowrisk_final.csv", index=False, encoding="utf-8-sig")
# print("\nSaved → sfda_Lowrisk_final.csv")