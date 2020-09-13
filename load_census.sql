CREATE TABLE sketch.acs_vrenduch (
	"State" DECIMAL NOT NULL, 
	"County" DECIMAL NOT NULL, 
	"County_name" VARCHAR NOT NULL, 
	"Block_Group" DECIMAL NOT NULL, 
	"avg_Agg_HH_INC_ACS_14_18" DECIMAL, 
	"avg_Agg_House_Value_ACS_14_18" DECIMAL, 
	"avg_Tot_Prns_in_HHD_ACS_14_18" DECIMAL, 
	"Crowd_Occp_U_ACS_14_18" DECIMAL NOT NULL, 
	"ENG_VW_ACS_14_18" DECIMAL NOT NULL, 
	"Female_No_HB_ACS_14_18" DECIMAL NOT NULL, 
	"Females_ACS_14_18" DECIMAL NOT NULL, 
	"Hispanic_ACS_14_18" DECIMAL NOT NULL, 
	"LAND_AREA" DECIMAL NOT NULL, 
	"Males_ACS_14_18" DECIMAL NOT NULL, 
	"Med_HHD_Inc_BG_ACS_14_18" DECIMAL, 
	"Median_Age_ACS_14_18" DECIMAL, 
	"MrdCple_Fmly_HHD_ACS_14_18" DECIMAL NOT NULL, 
	"NH_AIAN_alone_ACS_14_18" DECIMAL NOT NULL, 
	"NonFamily_HHD_ACS_14_18" DECIMAL NOT NULL, 
	"Not_HS_Grad_ACS_14_18" DECIMAL NOT NULL
);

\copy sketch.acs_vrenduch from program 'awk FNR-1 /data/groups/bills3/vrenduch/*.csv | cat' DELIMITER ',' CSV HEADER;