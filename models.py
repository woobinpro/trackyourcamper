# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Migrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    contextkey = models.CharField(db_column='ContextKey', max_length=300, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__migrationhistory'


class Aspnetroles(models.Model):
    id = models.CharField(db_column='Id', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aspnetroles'


class Aspnetuserclaims(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    claimtype = models.TextField(db_column='ClaimType', blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.TextField(db_column='ClaimValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aspnetuserclaims'


class Aspnetuserlogins(models.Model):
    loginprovider = models.CharField(db_column='LoginProvider', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    providerkey = models.CharField(db_column='ProviderKey', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aspnetuserlogins'


class Aspnetuserroles(models.Model):
    userid = models.CharField(db_column='UserId', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleId', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aspnetuserroles'


class Aspnetusers(models.Model):
    id = models.CharField(db_column='Id', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    emailconfirmed = models.IntegerField(db_column='EmailConfirmed', blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.TextField(db_column='PasswordHash', blank=True, null=True)  # Field name made lowercase.
    securitystamp = models.TextField(db_column='SecurityStamp', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    phonenumberconfirmed = models.IntegerField(db_column='PhoneNumberConfirmed', blank=True, null=True)  # Field name made lowercase.
    twofactorenabled = models.IntegerField(db_column='TwoFactorEnabled', blank=True, null=True)  # Field name made lowercase.
    lockoutenddateutc = models.DateTimeField(db_column='LockoutEndDateUtc', blank=True, null=True)  # Field name made lowercase.
    lockoutenabled = models.IntegerField(db_column='LockoutEnabled', blank=True, null=True)  # Field name made lowercase.
    accessfailedcount = models.IntegerField(db_column='AccessFailedCount', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=256, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aspnetusers'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Billingaddressmaster(models.Model):
    id = models.IntegerField(blank=True, null=True)
    userid = models.CharField(db_column='UserID', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    salutation = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(db_column='Firstname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=250, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    company_addition = models.CharField(db_column='Company_addition', max_length=250, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    road = models.CharField(db_column='Road', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    housenumber = models.CharField(db_column='Housenumber', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    additionaladdress = models.CharField(db_column='Additionaladdress', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    state = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    postcode = models.CharField(db_column='Postcode', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    vatnumber = models.CharField(db_column='VATnumber', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billingaddressmaster'


class Brandmodeltypeset(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    iscustom = models.IntegerField(db_column='IsCustom', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brandmodeltypeset'


class Brandset(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brandset'


class CMigrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    contextkey = models.CharField(db_column='ContextKey', max_length=300, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c__migrationhistory'


class CamperRegulationansmaster(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    anstype = models.CharField(db_column='Anstype', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'camper_regulationansmaster'


class Campingplaces(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    qwnerid = models.IntegerField(db_column='QwnerId', blank=True, null=True)  # Field name made lowercase.
    regulations_acsiclubcardacceptedasproofofidentity = models.IntegerField(db_column='regulations_ACSIClubCardAcceptedasProofofIdentity', blank=True, null=True)  # Field name made lowercase.
    regulations_passportidentitycardrequired = models.IntegerField(db_column='regulations_Passportidentitycardrequired', blank=True, null=True)  # Field name made lowercase.
    regulations_seniorcitizendiscount = models.IntegerField(blank=True, null=True)
    regulations_paymentbycreditcardpossible = models.IntegerField(db_column='regulations_Paymentbycreditcardpossible', blank=True, null=True)  # Field name made lowercase.
    regulations_paymentbydebitcard_maestropossible = models.IntegerField(db_column='regulations_Paymentbydebitcard_Maestropossible', blank=True, null=True)  # Field name made lowercase.
    regulations_duringthenoonbreakentranceprohibited = models.IntegerField(db_column='regulations_Duringthenoonbreakentranceprohibited', blank=True, null=True)  # Field name made lowercase.
    regulations_carfreeparkingspace = models.IntegerField(db_column='regulations_Carfreeparkingspace', blank=True, null=True)  # Field name made lowercase.
    regulations_nodogsallowedinlowseason = models.IntegerField(db_column='regulations_Nodogsallowedinlowseason', blank=True, null=True)  # Field name made lowercase.
    regulations_only1dog_leashed_allowedinlowseason = models.IntegerField(db_column='regulations_Only1dog_leashed_allowedinlowseason', blank=True, null=True)  # Field name made lowercase.
    regulations_severaldogs_leashed_allowedinlowseason = models.IntegerField(db_column='regulations_Severaldogs_leashed_allowedinlowseason', blank=True, null=True)  # Field name made lowercase.
    regulations_nodogsallowedinhighseason = models.IntegerField(db_column='regulations_Nodogsallowedinhighseason', blank=True, null=True)  # Field name made lowercase.
    regulations_only1dog_leashed_allowedinthehighseason = models.IntegerField(db_column='regulations_Only1dog_leashed_allowedinthehighseason', blank=True, null=True)  # Field name made lowercase.
    regualtions_severaldogs_leashed_allowedinthehighseason = models.IntegerField(db_column='regualtions_Severaldogs_leashed_allowedinthehighseason', blank=True, null=True)  # Field name made lowercase.
    regualtions_tentsallowed = models.IntegerField(db_column='regualtions_Tentsallowed', blank=True, null=True)  # Field name made lowercase.
    regualtions_caravanallowed = models.IntegerField(db_column='regualtions_Caravanallowed', blank=True, null=True)  # Field name made lowercase.
    regualtions_alsosuitableforcaravans_5_5mexclusivedrawbar = models.IntegerField(db_column='regualtions_Alsosuitableforcaravans_5_5mexclusivedrawbar', blank=True, null=True)  # Field name made lowercase.
    regualtions_doubleaxleallowed = models.IntegerField(db_column='regualtions_Doubleaxleallowed', blank=True, null=True)  # Field name made lowercase.
    regualtions_motorhomesallowed = models.IntegerField(db_column='regualtions_Motorhomesallowed', blank=True, null=True)  # Field name made lowercase.
    regualtions_alsomotorhomessuitable8mand4000kg = models.IntegerField(db_column='regualtions_Alsomotorhomessuitable8mand4000kg', blank=True, null=True)  # Field name made lowercase.
    regualtions_smalladditionaltentallowed = models.IntegerField(db_column='regualtions_Smalladditionaltentallowed', blank=True, null=True)  # Field name made lowercase.
    regualtions_adaccampingcardaccepted = models.IntegerField(db_column='regualtions_ADACCampingCardAccepted', blank=True, null=True)  # Field name made lowercase.
    regualtions_adackeyeuropecardaccepted = models.IntegerField(db_column='regualtions_ADACKeyEuropeCardAccepted', blank=True, null=True)  # Field name made lowercase.
    regualtions_acsicardakzeptiert = models.IntegerField(db_column='regualtions_ACSICardAkzeptiert', blank=True, null=True)  # Field name made lowercase.
    regualtions_ccicardaccepted = models.IntegerField(db_column='regualtions_CCICardAccepted', blank=True, null=True)  # Field name made lowercase.
    regualtions_myplacecardaccepted = models.IntegerField(db_column='regualtions_MyPlaceCardAccepted', blank=True, null=True)  # Field name made lowercase.
    regualtions_bestdealcampingcard = models.IntegerField(db_column='regualtions_BestDealCampingCard', blank=True, null=True)  # Field name made lowercase.
    regulations_topcampingcard = models.IntegerField(db_column='regulations_TopCampingCard', blank=True, null=True)  # Field name made lowercase.
    regualtions_anwbdetectivecampingcard = models.IntegerField(db_column='regualtions_anwbDetectiveCampingCard', blank=True, null=True)  # Field name made lowercase.
    address_city = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    address_country = models.CharField(db_column='address_Country', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_road = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    address_postcode = models.CharField(db_column='address_PostCode', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_state = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    address_degreeoflatitude = models.FloatField(blank=True, null=True)
    address_degreeoflongitude = models.FloatField(blank=True, null=True)
    contactdetails_phone = models.CharField(max_length=20, db_collation='utf8_general_ci', blank=True, null=True)
    contactdetails_email = models.CharField(db_column='contactdetails_Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    basedata_wlan = models.IntegerField(db_column='basedata_WLAN', blank=True, null=True)  # Field name made lowercase.
    basedata_acsicardavailable = models.IntegerField(db_column='basedata_ACSIcardavailable', blank=True, null=True)  # Field name made lowercase.
    basedata_acsiclubid = models.CharField(db_column='basedata_ACSIClubID', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    basedata_routedescription = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    basedata_wintercamping = models.IntegerField(db_column='basedata_Wintercamping', blank=True, null=True)  # Field name made lowercase.
    basedata_wheelchairaccessible = models.IntegerField(db_column='basedata_Wheelchairaccessible', blank=True, null=True)  # Field name made lowercase.
    basedata_fkk = models.IntegerField(db_column='basedata_FKK', blank=True, null=True)  # Field name made lowercase.
    basedata_powerprotectionina = models.IntegerField(db_column='basedata_PowerprotectioninA', blank=True, null=True)  # Field name made lowercase.
    basedata_europlug = models.IntegerField(blank=True, null=True)
    basedata_heightofthecampsite = models.CharField(db_column='basedata_Heightofthecampsite', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    basedata_areaofthecampsite = models.CharField(db_column='basedata_Areaofthecampsite', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    basedata_numberoftouristplaces = models.IntegerField(db_column='basedata_Numberoftouristplaces', blank=True, null=True)  # Field name made lowercase.
    basedata_numberofrentalproperties_permanentcampers = models.IntegerField(db_column='basedata_Numberofrentalproperties_permanentcampers', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_nearamotorwayexit_10km = models.IntegerField(db_column='Locationsoilplants_Nearamotorwayexit_10km', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_locatedintheforest = models.IntegerField(db_column='Locationsoilplants_Locatedintheforest', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_locatedontheriverorstream_maxkm = models.IntegerField(db_column='Locationsoilplants_Locatedontheriverorstream_maxkm', blank=True, null=True)  # Field name made lowercase.
    locationsiloplants_locatedonarecreationallake_maxkm = models.IntegerField(db_column='Locationsiloplants_Locatedonarecreationallake_maxkm', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_locatedbythesea_within_km = models.IntegerField(db_column='Locationsoilplants_Locatedbythesea_within_km', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_panorama = models.IntegerField(db_column='Locationsoilplants_panorama', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_lawn = models.IntegerField(db_column='Locationsoilplants_lawn', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_sandybeach = models.IntegerField(db_column='Locationsoilplants_sandybeach', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_beacharea = models.IntegerField(db_column='Locationsoilplants_beacharea', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_gravelbeach = models.IntegerField(db_column='Locationsoilplants_gravelbeach', blank=True, null=True)  # Field name made lowercase.
    locationssoilplants_stonybeach = models.IntegerField(db_column='Locationssoilplants_Stonybeach', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_artificiallyfortifiedbeach = models.IntegerField(db_column='Locationsoilplants_Artificiallyfortifiedbeach', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_rockycoast = models.IntegerField(db_column='Locationsoilplants_rockycoast', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_forcaravans_motorhomesdifficulttoaccess = models.IntegerField(db_column='Locationsoilplants_Forcaravans_motorhomesdifficulttoaccess', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_public_transportwithinashortdistance_maxkm = models.IntegerField(db_column='Locationsoilplants_Public_Transportwithinashortdistance_maxkm', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_grass = models.IntegerField(db_column='Locationsoilplants_grass', blank=True, null=True)  # Field name made lowercase.
    locationssoilplants_sandysoil = models.IntegerField(db_column='Locationssoilplants_sandysoil', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_hardground = models.IntegerField(db_column='Locationsoilplants_Hardground', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_attachedparkingspace = models.IntegerField(db_column='Locationsoilplants_Attachedparkingspace', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_terracedsite = models.IntegerField(db_column='Locationsoilplants_terracedsite', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_hillside = models.IntegerField(db_column='Locationsoilplants_hillside', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_parceledpitches = models.IntegerField(db_column='Locationsoilplants_Parceledpitches', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_placeswithoutshade = models.IntegerField(db_column='Locationsoilplants_Placeswithoutshade', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_placeswithsomeshade = models.IntegerField(db_column='Locationsoilplants_Placeswithsomeshade', blank=True, null=True)  # Field name made lowercase.
    locationsoilplants_placeswithalotofshade = models.IntegerField(db_column='Locationsoilplants_Placeswithalotofshade', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_someplaygroundequipment = models.IntegerField(db_column='Sportsandgames_Someplaygroundequipment', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_childrensplayground = models.IntegerField(db_column='Sportsandgames_ChildrensPlayground', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_indoorplayground = models.IntegerField(db_column='Sportsandgames_Indoorplayground', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_waterplayground = models.IntegerField(db_column='Sportsandgames_Waterplayground', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_mulitsportfeld = models.IntegerField(db_column='Sportsandgames_Mulitsportfeld', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_beachvolleyball = models.IntegerField(db_column='Sportsandgames_Beachvolleyball', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_horsebackriding = models.IntegerField(db_column='Sportsandgames_Horsebackriding', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_riding_pony = models.IntegerField(db_column='Sportsandgames_Riding_pony', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_minigolf = models.IntegerField(db_column='Sportsandgames_Minigolf', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_golfcourse_min6holes = models.IntegerField(db_column='Sportsandgames_Golfcourse_min6holes', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_golfcoursewithinashortdistance_max10km = models.IntegerField(db_column='Sportsandgames_Golfcoursewithinashortdistance_max10km', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_tabletennis = models.IntegerField(db_column='Sportsandgames_Tabletennis', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_tennis = models.IntegerField(db_column='Sportsandgames_Tennis', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_tennislessons = models.IntegerField(db_column='Sportsandgames_Tennislessons', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_squash = models.IntegerField(db_column='Sportsandgames_squash', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_bowlingand_orbowlingalley = models.IntegerField(db_column='Sportsandgames_Bowlingand_orbowlingalley', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_boccia = models.IntegerField(db_column='Sportsandgames_Boccia', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_archery = models.IntegerField(db_column='Sportsandgames_archery', blank=True, null=True)  # Field name made lowercase.
    sportsandgmaes_trampoline = models.IntegerField(db_column='Sportsandgmaes_trampoline', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_bouncy = models.IntegerField(db_column='Sportsandgames_bouncy', blank=True, null=True)  # Field name made lowercase.
    sportsandgames_climbingwall = models.IntegerField(db_column='Sportsandgames_climbingwall', blank=True, null=True)  # Field name made lowercase.
    sportsandgmaes_geocaching = models.IntegerField(db_column='Sportsandgmaes_Geocaching', blank=True, null=True)  # Field name made lowercase.
    rw_excursionprogram_atleasttwiceaweekhighseason = models.IntegerField(db_column='Rw_Excursionprogram_atleasttwiceaweekhighseason', blank=True, null=True)  # Field name made lowercase.
    rw_aniforchildupto12y_atleasttwiceaweekinhighseason = models.IntegerField(db_column='Rw_Aniforchildupto12y_atleasttwiceaweekinhighseason', blank=True, null=True)  # Field name made lowercase.
    rw_aniforchildupto13_18y_atleasttwiceaweekinhighseason = models.IntegerField(db_column='Rw_Aniforchildupto13_18y_atleasttwiceaweekinhighseason', blank=True, null=True)  # Field name made lowercase.
    rw_aniforadults_atleasttwiceaweekinhighseason = models.IntegerField(db_column='Rw_Aniforadults_atleasttwiceaweekinhighseason', blank=True, null=True)  # Field name made lowercase.
    rw_guidedwalks = models.IntegerField(db_column='Rw_Guidedwalks', blank=True, null=True)  # Field name made lowercase.
    rw_markedfußwandereungenthecampsite = models.IntegerField(db_column='Rw_MarkedFußwandereungenthecampsite', blank=True, null=True)  # Field name made lowercase.
    rw_gpswalks = models.IntegerField(db_column='Rw_GPSwalks', blank=True, null=True)  # Field name made lowercase.
    rw_amcampingplatzbeginnendefahrradrouten = models.IntegerField(db_column='Rw_AmCampingplatzbeginnendeFahrradrouten', blank=True, null=True)  # Field name made lowercase.
    rw_sittingroom = models.IntegerField(db_column='Rw_sittingroom', blank=True, null=True)  # Field name made lowercase.
    rw_daycarecenter = models.IntegerField(db_column='Rw_daycarecenter', blank=True, null=True)  # Field name made lowercase.
    rw_animalmeadow = models.IntegerField(db_column='Rw_animalmeadow', blank=True, null=True)  # Field name made lowercase.
    rw_miniclub_mind_4x_wöchentlich_hochsaison = models.IntegerField(db_column='Rw_Miniclub_mind_4x_wöchentlich_Hochsaison', blank=True, null=True)  # Field name made lowercase.
    rw_discotheque = models.IntegerField(db_column='Rw_Discotheque', blank=True, null=True)  # Field name made lowercase.
    rw_discoevenings = models.IntegerField(db_column='Rw_Discoevenings', blank=True, null=True)  # Field name made lowercase.
    rw_watchtv = models.IntegerField(db_column='Rw_watchTV', blank=True, null=True)  # Field name made lowercase.
    rw_slots = models.IntegerField(db_column='Rw_slots', blank=True, null=True)  # Field name made lowercase.
    rw_pool_billiards = models.IntegerField(db_column='Rw_Pool_Billiards', blank=True, null=True)  # Field name made lowercase.
    rw_gym = models.IntegerField(db_column='Rw_gym', blank=True, null=True)  # Field name made lowercase.
    rw_solarium = models.IntegerField(db_column='Rw_solarium', blank=True, null=True)  # Field name made lowercase.
    rw_sauna = models.IntegerField(db_column='Rw_sauna', blank=True, null=True)  # Field name made lowercase.
    rw_whirlpool = models.IntegerField(db_column='Rw_Whirlpool', blank=True, null=True)  # Field name made lowercase.
    rw_steambath = models.IntegerField(db_column='Rw_steambath', blank=True, null=True)  # Field name made lowercase.
    rw_thermalbaths = models.IntegerField(db_column='Rw_thermalbaths', blank=True, null=True)  # Field name made lowercase.
    rw_massage = models.IntegerField(db_column='Rw_Massage', blank=True, null=True)  # Field name made lowercase.
    rw_hydromassage = models.IntegerField(db_column='Rw_Hydromassage', blank=True, null=True)  # Field name made lowercase.
    rw_beautycenter = models.IntegerField(db_column='Rw_BeautyCenter', blank=True, null=True)  # Field name made lowercase.
    sr_freshbreadavailableatthecampsite = models.IntegerField(db_column='Sr_Freshbreadavailableatthecampsite', blank=True, null=True)  # Field name made lowercase.
    sr_foodrestrictedavailable = models.IntegerField(db_column='Sr_Foodrestrictedavailable', blank=True, null=True)  # Field name made lowercase.
    sr_foodgreatchoice = models.IntegerField(db_column='Sr_Foodgreatchoice', blank=True, null=True)  # Field name made lowercase.
    sr_snack = models.IntegerField(db_column='Sr_snack', blank=True, null=True)  # Field name made lowercase.
    sr_takeawayfood = models.IntegerField(db_column='Sr_Takeawayfood', blank=True, null=True)  # Field name made lowercase.
    sr_pizzeria = models.IntegerField(db_column='Sr_pizzeria', blank=True, null=True)  # Field name made lowercase.
    sr_bar = models.IntegerField(db_column='Sr_Bar', blank=True, null=True)  # Field name made lowercase.
    sr_sbrestaurant = models.IntegerField(db_column='Sr_SBRestaurant', blank=True, null=True)  # Field name made lowercase.
    sr_restaurant_withsmallmenu = models.IntegerField(db_column='Sr_Restaurant_withsmallmenu', blank=True, null=True)  # Field name made lowercase.
    sr_restaurant_withbigmap = models.IntegerField(db_column='Sr_Restaurant_withbigmap', blank=True, null=True)  # Field name made lowercase.
    sr_gasavailable = models.IntegerField(db_column='Sr_Gasavailable', blank=True, null=True)  # Field name made lowercase.
    sr_freezingthecoolingelements = models.IntegerField(db_column='Sr_Freezingthecoolingelements', blank=True, null=True)  # Field name made lowercase.
    sr_cooliceavailable = models.IntegerField(db_column='Sr_Cooliceavailable', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_outdoorpool = models.IntegerField(db_column='Relaxationatthewater_outdoorpool', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_outdoorheatedpool = models.IntegerField(db_column='Relaxationatthewater_Outdoorheatedpool', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_sunroofnatatorium = models.IntegerField(db_column='Relaxationatthewater_SunroofNatatorium', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_sunroofswimmingpoolheated = models.IntegerField(db_column='Relaxationatthewater_Sunroofswimmingpoolheated', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_childrenspool_for1_3yearolds_40cm = models.IntegerField(db_column='Relaxationatthewater_Childrenspool_for1_3yearolds_40cm', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_heatedpoolforchildren = models.IntegerField(db_column='Relaxationatthewater_Heatedpoolforchildren', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_waterslide_10m = models.IntegerField(db_column='Relaxationatthewater_Waterslide_10m', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_waterpark = models.IntegerField(db_column='Relaxationatthewater_Waterpark', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_swimmingintheriver_streammaxkm = models.IntegerField(db_column='Relaxationatthewater_Swimmingintheriver_streammaxkm', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_swimminginthesea_maxkm = models.IntegerField(db_column='Relaxationatthewater_Swimminginthesea_maxkm', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_bathinginarecreational_bathinglake_maxkm = models.IntegerField(db_column='Relaxationatthewater_Bathinginarecreational_bathinglake_maxkm', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_beachshowers = models.IntegerField(db_column='Relaxationatthewater_beachshowers', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_fishing = models.IntegerField(db_column='Relaxationatthewater_fishing', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_diving = models.IntegerField(db_column='Relaxationatthewater_diving', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_snorkelling = models.IntegerField(db_column='Relaxationatthewater_Snorkelling', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_windsurfingallowed = models.IntegerField(db_column='Relaxationatthewater_Windsurfingallowed', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_windsurfingcourse = models.IntegerField(db_column='Relaxationatthewater_Windsurfingcourse', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_sailingallowed = models.IntegerField(db_column='Relaxationatthewater_Sailingallowed', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_segelkurs = models.IntegerField(db_column='Relaxationatthewater_Segelkurs', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_rafting_kayaking_rafting = models.IntegerField(db_column='Relaxationatthewater_Rafting_kayaking_rafting', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_kayakingcourse = models.IntegerField(db_column='Relaxationatthewater_kayakingcourse', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_waterskiingallowed = models.IntegerField(db_column='Relaxationatthewater_Waterskiingallowed', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_ownboatallowed = models.IntegerField(db_column='Relaxationatthewater_Ownboatallowed', blank=True, null=True)  # Field name made lowercase.
    relaxationatthewater_boatslip = models.IntegerField(db_column='Relaxationatthewater_Boatslip', blank=True, null=True)  # Field name made lowercase.
    washingup_dishwasherwithcoldwater = models.IntegerField(db_column='Washingup_Dishwasherwithcoldwater', blank=True, null=True)  # Field name made lowercase.
    washingup_dishwasherwithhotwater = models.IntegerField(db_column='Washingup_Dishwasherwithhotwater', blank=True, null=True)  # Field name made lowercase.
    washingup_dishwasher = models.IntegerField(db_column='Washingup_dishwasher', blank=True, null=True)  # Field name made lowercase.
    washingup_laundrysinkwithcoldwater = models.IntegerField(db_column='Washingup_Laundrysinkwithcoldwater', blank=True, null=True)  # Field name made lowercase.
    washingup_laundrysinkwithhotwater = models.IntegerField(db_column='Washingup_Laundrysinkwithhotwater', blank=True, null=True)  # Field name made lowercase.
    washingup_washingmachine = models.IntegerField(db_column='Washingup_Washingmachine', blank=True, null=True)  # Field name made lowercase.
    washingup_clothesdryer = models.IntegerField(db_column='Washingup_clothesdryer', blank=True, null=True)  # Field name made lowercase.
    washingup_roningfacilities = models.IntegerField(db_column='Washingup_roningfacilities', blank=True, null=True)  # Field name made lowercase.
    washingup_individualcookingopportunity = models.IntegerField(db_column='Washingup_Individualcookingopportunity', blank=True, null=True)  # Field name made lowercase.
    washingup_cookingfacilitiesforgroups = models.IntegerField(db_column='Washingup_Cookingfacilitiesforgroups', blank=True, null=True)  # Field name made lowercase.
    washingup_microwave = models.IntegerField(db_column='Washingup_microwave', blank=True, null=True)  # Field name made lowercase.
    si_sink_coldwater = models.IntegerField(db_column='Si_Sink_coldwater', blank=True, null=True)  # Field name made lowercase.
    si_sink_warmwater = models.IntegerField(db_column='Si_Sink_warmwater', blank=True, null=True)  # Field name made lowercase.
    si_singlewashcabins_coldwater = models.IntegerField(db_column='Si_Singlewashcabins_coldwater', blank=True, null=True)  # Field name made lowercase.
    si_singlewashcabins_warmwater = models.IntegerField(db_column='Si_Singlewashcabins_warmwater', blank=True, null=True)  # Field name made lowercase.
    si_showers_coldwater = models.IntegerField(db_column='Si_Showers_coldwater', blank=True, null=True)  # Field name made lowercase.
    si_showers_warmwater = models.IntegerField(db_column='Si_Showers_warmwater', blank=True, null=True)  # Field name made lowercase.
    si_familyshowers = models.IntegerField(db_column='Si_familyshowers', blank=True, null=True)  # Field name made lowercase.
    si_seniorshower_withextraholders = models.IntegerField(db_column='Si_Seniorshower_withextraholders', blank=True, null=True)  # Field name made lowercase.
    si_familysanitary = models.IntegerField(db_column='Si_familysanitary', blank=True, null=True)  # Field name made lowercase.
    si_heatedtoilets = models.IntegerField(db_column='Si_Heatedtoilets', blank=True, null=True)  # Field name made lowercase.
    si_childrenssanitary = models.IntegerField(db_column='Si_childrenssanitary', blank=True, null=True)  # Field name made lowercase.
    si_privatesanitary = models.IntegerField(db_column='Si_privatesanitary', blank=True, null=True)  # Field name made lowercase.
    si_privatetoilet = models.IntegerField(db_column='Si_privatetoilet', blank=True, null=True)  # Field name made lowercase.
    si_toiletseat = models.IntegerField(db_column='Si_toiletseat', blank=True, null=True)  # Field name made lowercase.
    si_frenchtoilet = models.IntegerField(db_column='Si_Frenchtoilet', blank=True, null=True)  # Field name made lowercase.
    si_toiletfortheelderly = models.IntegerField(db_column='Si_toiletfortheelderly', blank=True, null=True)  # Field name made lowercase.
    si_toiletpaperavailable = models.IntegerField(db_column='Si_Toiletpaperavailable', blank=True, null=True)  # Field name made lowercase.
    si_spoutforchemicaltoilet = models.IntegerField(db_column='Si_Spoutforchemicaltoilet', blank=True, null=True)  # Field name made lowercase.
    si_changingroom = models.IntegerField(db_column='Si_changingroom', blank=True, null=True)  # Field name made lowercase.
    si_waterconnectionon_atthepitch_max15m = models.IntegerField(db_column='Si_Waterconnectionon_atthepitch_max15m', blank=True, null=True)  # Field name made lowercase.
    si_wastewaterdischarge_parkingspace_max15m = models.IntegerField(db_column='Si_Wastewaterdischarge_parkingspace_max15m', blank=True, null=True)  # Field name made lowercase.
    si_waterpointon_atthepitch_max15m = models.IntegerField(db_column='Si_Waterpointon_atthepitch_max15m', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_tents = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_lodgetentwithoutplumbing = models.IntegerField(db_column='sportaccessoriesrental_Lodgetentwithoutplumbing', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_lodgetentwithplumbing = models.IntegerField(db_column='sportaccessoriesrental_Lodgetentwithplumbing', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_caravan = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_mobilehomes = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_cabins = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_room = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_studios = models.IntegerField(db_column='sportaccessoriesrental_Studios', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_apartments = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_bungalow_chalets = models.IntegerField(db_column='sportaccessoriesrental_Bungalow_Chalets', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_coolingfan = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_safes = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_surfboards = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_motorboats = models.IntegerField(db_column='sportaccessoriesrental_Motorboats', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_sailboats = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_rowboats = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_canoes = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_kayaks = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_rentalofexchangeequipment = models.IntegerField(db_column='sportaccessoriesrental_Rentalofexchangeequipment', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_pedalboats = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_mountainbikes = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_cycles = models.IntegerField(db_column='sportaccessoriesrental_Cycles', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_e_bikes = models.IntegerField(db_column='sportaccessoriesrental_E_Bikes', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_scooter = models.IntegerField(blank=True, null=True)
    sportaccessoriesrental_kettcar_pedalcar = models.IntegerField(db_column='sportaccessoriesrental_Kettcar_pedalcar', blank=True, null=True)  # Field name made lowercase.
    sportaccessoriesrental_cars = models.IntegerField(blank=True, null=True)
    general_germanspokenatthereception_inhighseason = models.IntegerField(db_column='General_Germanspokenatthereception_inhighseason', blank=True, null=True)  # Field name made lowercase.
    general_reservationinhighseasonisrecommended = models.IntegerField(db_column='General_Reservationinhighseasonisrecommended', blank=True, null=True)  # Field name made lowercase.
    general_reservationinlowseasonisrecommended = models.IntegerField(db_column='General_Reservationinlowseasonisrecommended', blank=True, null=True)  # Field name made lowercase.
    general_reservationpossiblewithcampingcardacsi = models.IntegerField(db_column='General_ReservationpossiblewithCampingCardACSI', blank=True, null=True)  # Field name made lowercase.
    general_pitcheswithradioandtvconnection = models.IntegerField(db_column='General_PitcheswithradioandTVconnection', blank=True, null=True)  # Field name made lowercase.
    general_specialpitchesforcampers = models.IntegerField(db_column='General_Specialpitchesforcampers', blank=True, null=True)  # Field name made lowercase.
    general_supplyanddisposalstationformotorhomes = models.IntegerField(db_column='General_Supplyanddisposalstationformotorhomes', blank=True, null=True)  # Field name made lowercase.
    general_fieldlighting = models.IntegerField(db_column='General_fieldlighting', blank=True, null=True)  # Field name made lowercase.
    general_guardedterrain = models.IntegerField(db_column='General_Guardedterrain', blank=True, null=True)  # Field name made lowercase.
    general_quietduringthedayandatnight = models.IntegerField(db_column='General_Quietduringthedayandatnight', blank=True, null=True)  # Field name made lowercase.
    general_onlyquietatnight = models.IntegerField(db_column='General_Onlyquietatnight', blank=True, null=True)  # Field name made lowercase.
    general_separateyouthplace = models.IntegerField(db_column='General_Separateyouthplace', blank=True, null=True)  # Field name made lowercase.
    general_dogwalkingarea = models.IntegerField(db_column='General_Dogwalkingarea', blank=True, null=True)  # Field name made lowercase.
    general_internetaccess = models.IntegerField(db_column='General_Internetaccess', blank=True, null=True)  # Field name made lowercase.
    general_wifi_wifihotspot = models.IntegerField(db_column='General_Wifi_Wifihotspot', blank=True, null=True)  # Field name made lowercase.
    general_w_lan_wifi_80 = models.IntegerField(db_column='General_W_LAN_Wifi_80', blank=True, null=True)  # Field name made lowercase.
    general_campinginfoapp = models.IntegerField(db_column='General_CampingInfoApp', blank=True, null=True)  # Field name made lowercase.
    general_anykindofbarbecueallowed = models.IntegerField(db_column='General_Anykindofbarbecueallowed', blank=True, null=True)  # Field name made lowercase.
    general_charcoalgrillallowed = models.IntegerField(db_column='General_Charcoalgrillallowed', blank=True, null=True)  # Field name made lowercase.
    general_gasgrillallowed = models.IntegerField(db_column='General_Gasgrillallowed', blank=True, null=True)  # Field name made lowercase.
    general_electricgrillallowed = models.IntegerField(db_column='General_Electricgrillallowed', blank=True, null=True)  # Field name made lowercase.
    general_commonshaftgrill = models.IntegerField(db_column='General_CommonshaftGrill', blank=True, null=True)  # Field name made lowercase.
    general_temporarilyoutside_cpslocatedwithoutpower = models.IntegerField(db_column='General_Temporarilyoutside_CPslocatedwithoutpower', blank=True, null=True)  # Field name made lowercase.
    general_temporarilyoutside_ofthecpswithelectricity = models.IntegerField(db_column='General_Temporarilyoutside_oftheCPswithelectricity', blank=True, null=True)  # Field name made lowercase.
    general_atmcashwithdrawalspossible = models.IntegerField(db_column='General_ATMcashwithdrawalspossible', blank=True, null=True)  # Field name made lowercase.
    general_defibrillator = models.IntegerField(db_column='General_defibrillator', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campingplaces'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Merchantbrands(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    merchantid = models.IntegerField(db_column='MerchantId', blank=True, null=True)  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merchantbrands'


class Merchants(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_city = models.CharField(db_column='Address_City', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_country = models.CharField(db_column='Address_Country', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_street = models.CharField(db_column='Address_Street', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_postal = models.CharField(db_column='Address_Postal', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_state = models.CharField(db_column='Address_State', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_latitude = models.FloatField(db_column='Address_Latitude', blank=True, null=True)  # Field name made lowercase.
    address_longitude = models.FloatField(db_column='Address_Longitude', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    installationflatrate = models.DecimalField(db_column='Installationflatrate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    supportedbrand = models.IntegerField(db_column='Supportedbrand', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_mondaystart = models.CharField(db_column='OpenTimes_OpenTimes_MondayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_mondayend = models.CharField(db_column='OpenTimes_OpenTimes_MondayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_tuesdaystart = models.CharField(db_column='OpenTimes_OpenTimes_TuesdayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_tuesdayend = models.CharField(db_column='OpenTimes_OpenTimes_TuesdayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_wednesdaystart = models.CharField(db_column='OpenTimes_OpenTimes_WednesdayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_wednesdayend = models.CharField(db_column='OpenTimes_OpenTimes_WednesdayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_thursdaystart = models.CharField(db_column='OpenTimes_OpenTimes_ThursdayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_thursdayend = models.CharField(db_column='OpenTimes_OpenTimes_ThursdayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_fridaystart = models.CharField(db_column='OpenTimes_OpenTimes_FridayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_fridayend = models.CharField(db_column='OpenTimes_OpenTimes_FridayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_saturdaystart = models.CharField(db_column='OpenTimes_OpenTimes_SaturdayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_saturdayend = models.CharField(db_column='OpenTimes_OpenTimes_SaturdayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_sundaystart = models.CharField(db_column='OpenTimes_OpenTimes_SundayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    opentimes_opentimes_sundayend = models.CharField(db_column='OpenTimes_OpenTimes_SundayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_mondaystart = models.CharField(db_column='Summer_OpenTimes_OpenTimes_MondayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_mondayend = models.CharField(db_column='Summer_OpenTimes_OpenTimes_MondayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_tuesdaystart = models.CharField(db_column='Summer_OpenTimes_OpenTimes_TuesdayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_tuesdayend = models.CharField(db_column='Summer_OpenTimes_OpenTimes_TuesdayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_wednesdaystart = models.CharField(db_column='Summer_OpenTimes_OpenTimes_WednesdayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_wednesdayend = models.CharField(db_column='Summer_OpenTimes_OpenTimes_WednesdayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_thursdaystart = models.CharField(db_column='Summer_OpenTimes_OpenTimes_ThursdayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_thursdayend = models.CharField(db_column='Summer_OpenTimes_OpenTimes_ThursdayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_fridaystart = models.CharField(db_column='Summer_OpenTimes_OpenTimes_FridayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_fridayend = models.CharField(db_column='Summer_OpenTimes_OpenTimes_FridayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_saturdaystart = models.CharField(db_column='Summer_OpenTimes_OpenTimes_SaturdayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_saturdayend = models.CharField(db_column='Summer_OpenTimes_OpenTimes_SaturdayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_sundaystart = models.CharField(db_column='Summer_OpenTimes_OpenTimes_SundayStart', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    summer_opentimes_opentimes_sundayend = models.CharField(db_column='Summer_OpenTimes_OpenTimes_SundayEnd', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    winter_monday_close = models.IntegerField(db_column='Winter_Monday_close', blank=True, null=True)  # Field name made lowercase.
    winter_tuseday_close = models.IntegerField(db_column='Winter_tuseday_close', blank=True, null=True)  # Field name made lowercase.
    winter_wednessday_close = models.IntegerField(db_column='Winter_wednessday_close', blank=True, null=True)  # Field name made lowercase.
    winter_thursday_close = models.IntegerField(db_column='Winter_thursday_close', blank=True, null=True)  # Field name made lowercase.
    winter_friday_cloas = models.IntegerField(db_column='Winter_friday_cloas', blank=True, null=True)  # Field name made lowercase.
    winter_saturday_close = models.IntegerField(db_column='Winter_saturday_close', blank=True, null=True)  # Field name made lowercase.
    winter_sunday_close = models.IntegerField(db_column='Winter_sunday_close', blank=True, null=True)  # Field name made lowercase.
    summer_monday_close = models.IntegerField(db_column='Summer_Monday_close', blank=True, null=True)  # Field name made lowercase.
    summer_tuseday_close = models.IntegerField(db_column='Summer_tuseday_close', blank=True, null=True)  # Field name made lowercase.
    summer_wednessday_close = models.IntegerField(db_column='Summer_wednessday_close', blank=True, null=True)  # Field name made lowercase.
    summer_thursday_close = models.IntegerField(db_column='Summer_thursday_close', blank=True, null=True)  # Field name made lowercase.
    summer_friday_close = models.IntegerField(db_column='Summer_friday_close', blank=True, null=True)  # Field name made lowercase.
    summer_saturday_close = models.IntegerField(db_column='Summer_saturday_close', blank=True, null=True)  # Field name made lowercase.
    summer_sunday_close = models.IntegerField(db_column='Summer_sunday_close', blank=True, null=True)  # Field name made lowercase.
    dealeremail = models.CharField(db_column='Dealeremail', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merchants'


class Packagelist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    packagename = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    packagename_german = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    extractingreadingthedata = models.IntegerField(db_column='Extractingreadingthedata', blank=True, null=True)  # Field name made lowercase.
    realtimemonitoring = models.IntegerField(db_column='Realtimemonitoring', blank=True, null=True)  # Field name made lowercase.
    livetracking = models.IntegerField(db_column='Livetracking', blank=True, null=True)  # Field name made lowercase.
    dealersearchinyourarea = models.IntegerField(db_column='Dealersearchinyourarea', blank=True, null=True)  # Field name made lowercase.
    alarmonpresssosbutton = models.IntegerField(db_column='AlarmonPressSOSbutton', blank=True, null=True)  # Field name made lowercase.
    alarmonoverspeed = models.IntegerField(db_column='Alarmonoverspeed', blank=True, null=True)  # Field name made lowercase.
    alarmatvibration = models.IntegerField(db_column='Alarmatvibration', blank=True, null=True)  # Field name made lowercase.
    alarmonleavinganarea_geofence = models.IntegerField(db_column='Alarmonleavinganarea_geofence', blank=True, null=True)  # Field name made lowercase.
    holidaymode_vehiclecannotbemonitoredonholidayifdesired = models.IntegerField(db_column='Holidaymode_vehiclecannotbemonitoredonholidayifdesired', blank=True, null=True)  # Field name made lowercase.
    alarmincluded_beforevehicleismoved_mustbeswitchedoff = models.IntegerField(db_column='Alarmincluded_beforevehicleismoved_mustbeswitchedoff', blank=True, null=True)  # Field name made lowercase.
    locationqueryperday = models.IntegerField(db_column='Locationqueryperday', blank=True, null=True)  # Field name made lowercase.
    archivehistoryofvehiclelocations = models.CharField(db_column='Archivehistoryofvehiclelocations', max_length=100, blank=True, null=True)  # Field name made lowercase.
    immediatereplacementserviceofthetracker = models.CharField(db_column='Immediatereplacementserviceofthetracker', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vehiclefleetmanagement_numberofvehicles = models.IntegerField(db_column='Vehiclefleetmanagement_numberofvehicles', blank=True, null=True)  # Field name made lowercase.
    support_service_starttime = models.CharField(db_column='Support_Service_StartTime', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    support_service_endtime = models.CharField(db_column='Support_Service_EndTime', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    bringbackservice = models.CharField(db_column='BringBackService', max_length=100, blank=True, null=True)  # Field name made lowercase.
    activationfeeoncepervehicle = models.DecimalField(db_column='Activationfeeoncepervehicle', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    annualpricepervehicle = models.DecimalField(db_column='Annualpricepervehicle', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mobilesimcardincl_dataroamingeumtl = models.DecimalField(db_column='MobileSIMcardincl_DataroamingEUmtl', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isallowpayment = models.IntegerField(db_column='Isallowpayment', blank=True, null=True)  # Field name made lowercase.
    pricemonthly = models.DecimalField(db_column='PriceMonthly', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricequarter = models.DecimalField(db_column='PriceQuarter', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricehalf = models.DecimalField(db_column='PriceHalf', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priceoneyear = models.DecimalField(db_column='PriceOneYear', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricetwoyear = models.DecimalField(db_column='PriceTwoYear', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bringbackservicefrom = models.CharField(db_column='BringBackServiceFrom', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    bringbackserviceup = models.CharField(db_column='BringBackServiceUp', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='Isactive', blank=True, null=True)  # Field name made lowercase.
    onrequest_txt = models.CharField(db_column='Onrequest_txt', max_length=250, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='Sortorder', blank=True, null=True)  # Field name made lowercase.
    eachadditionalvehicle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    noofvehicleallow = models.IntegerField(db_column='Noofvehicleallow', blank=True, null=True)  # Field name made lowercase.
    annualpricepervehicle1 = models.IntegerField(db_column='Annualpricepervehicle1', blank=True, null=True)  # Field name made lowercase.
    annualpricepervehicle2 = models.IntegerField(db_column='Annualpricepervehicle2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packagelist'


class PackagewisePaymenttype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    packageid = models.IntegerField(db_column='PackageID', blank=True, null=True)  # Field name made lowercase.
    paytypename = models.CharField(db_column='PaytypeName', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    paytypename_german = models.CharField(db_column='PaytypeName_german', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packagewise_paymenttype'


class Paymenttype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='Paymenttype', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    sandbox_braintree_planid = models.CharField(db_column='Sandbox_Braintree_PlanID', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    production_braintree_planid = models.CharField(db_column='Production_Braintree_PlanID', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymenttype'


class Postalcodemaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    osm_id = models.FloatField(blank=True, null=True)
    ort = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    plz = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    bundesland = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    land = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'postalcodemaster'


class Promotioncredit(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    subscriptionid = models.IntegerField(db_column='SubscriptionId', blank=True, null=True)  # Field name made lowercase.
    creditamt = models.DecimalField(db_column='CreditAmt', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    debitamt = models.DecimalField(db_column='DebitAmt', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promotioncredit'


class Registractiondetails(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='ContactPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    road = models.CharField(db_column='Road', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accquiredby = models.CharField(db_column='Accquiredby', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subscription_package = models.IntegerField(db_column='Subscription_Package', blank=True, null=True)  # Field name made lowercase.
    subscriptionpackage_price = models.DecimalField(db_column='Subscriptionpackage_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subscriptionprice_cuurency = models.CharField(db_column='Subscriptionprice_cuurency', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    trackerpackage = models.IntegerField(db_column='TrackerPackage', blank=True, null=True)  # Field name made lowercase.
    trackerpackage_price = models.DecimalField(db_column='Trackerpackage_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tracker_currency = models.CharField(db_column='Tracker_currency', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    paymentinterval = models.IntegerField(db_column='PaymentInterval', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'registractiondetails'


class Salutationmaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salutation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salutationmaster'


class Securitycompanies(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_city = models.CharField(db_column='Address_City', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_country = models.CharField(db_column='Address_Country', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_street = models.CharField(db_column='Address_Street', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_postal = models.CharField(db_column='Address_Postal', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_state = models.CharField(db_column='Address_State', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_latitude = models.FloatField(db_column='Address_Latitude', blank=True, null=True)  # Field name made lowercase.
    address_longitude = models.FloatField(db_column='Address_Longitude', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerId', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='ContactPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emergency = models.CharField(db_column='Emergency', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'securitycompanies'


class Shippingaddressmaster(models.Model):
    id = models.IntegerField(blank=True, null=True)
    userid = models.CharField(db_column='UserID', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    salutation = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(db_column='Firstname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=250, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    company_addition = models.CharField(db_column='Company_addition', max_length=250, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    road = models.CharField(db_column='Road', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    housenumber = models.CharField(db_column='Housenumber', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    additionaladdress = models.CharField(db_column='Additionaladdress', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    state = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    postcode = models.CharField(db_column='Postcode', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    vatnumber = models.CharField(db_column='VATnumber', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shippingaddressmaster'


class Shippingcharges(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shippingcharges = models.DecimalField(db_column='Shippingcharges', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shippingcharges'


class Shoppingcartitems(models.Model):
    cartitemid = models.IntegerField(db_column='CartItemID', blank=True, null=True)  # Field name made lowercase.
    cartid = models.CharField(db_column='CartID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trackercategoryid = models.IntegerField(db_column='TrackerCategoryId', blank=True, null=True)  # Field name made lowercase.
    trackercategory = models.CharField(db_column='TrackerCategory', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    trackerid = models.IntegerField(db_column='TrackerId', blank=True, null=True)  # Field name made lowercase.
    trackername = models.CharField(db_column='TrackerName', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='Unitprice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quentity = models.IntegerField(db_column='Quentity', blank=True, null=True)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='Totalprice', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    articleno = models.IntegerField(db_column='Articleno', blank=True, null=True)  # Field name made lowercase.
    trackerimage = models.CharField(db_column='TrackerImage', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shoppingcartitems'


class Shopusers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    salutation = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(db_column='Firstname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=250, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    company_addition = models.CharField(db_column='Company_Addition', max_length=250, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    road = models.CharField(db_column='Road', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    housenumber = models.CharField(db_column='HouseNumber', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    additionaladdress = models.CharField(db_column='Additionaladdress', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='Postcode', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    vatnumber = models.CharField(db_column='VATnumber', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shopusers'


class SubscriptionOffers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    activefrom = models.DateTimeField(db_column='ActiveFrom', blank=True, null=True)  # Field name made lowercase.
    activeuntil = models.DateTimeField(db_column='ActiveUntil', blank=True, null=True)  # Field name made lowercase.
    offername = models.CharField(db_column='OfferName', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    offerdescription = models.CharField(db_column='OfferDescription', max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subscriptionid = models.IntegerField(db_column='SubscriptionId', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_offers'


class Subscriptionuserdetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salutation = models.IntegerField(db_column='Salutation', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='ContactPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    road = models.CharField(db_column='Road', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accquiredby = models.CharField(db_column='Accquiredby', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subscription_packageid = models.IntegerField(db_column='Subscription_PackageId', blank=True, null=True)  # Field name made lowercase.
    subscription_packagename = models.CharField(db_column='Subscription_PackageName', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subscriptionpackage_price = models.DecimalField(db_column='Subscriptionpackage_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subscriptionprice_cuurency = models.CharField(db_column='Subscriptionprice_cuurency', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    paymentinterval = models.IntegerField(db_column='PaymentInterval', blank=True, null=True)  # Field name made lowercase.
    paymrntinterval_method = models.CharField(db_column='Paymrntinterval_method', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    paymentinterval_price = models.DecimalField(db_column='Paymentinterval_price', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    trackerid = models.IntegerField(db_column='TrackerId', blank=True, null=True)  # Field name made lowercase.
    trackername = models.CharField(db_column='Trackername', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    trackerprice = models.DecimalField(db_column='TrackerPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mobilecardcharges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createddate = models.DateTimeField(db_column='Createddate', blank=True, null=True)  # Field name made lowercase.
    ispendingtraker_payment = models.IntegerField(db_column='Ispendingtraker_Payment', blank=True, null=True)  # Field name made lowercase.
    isactivesubscription = models.IntegerField(db_column='Isactivesubscription', blank=True, null=True)  # Field name made lowercase.
    subscription_transactionid = models.CharField(db_column='Subscription_transactionID', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    tracker_tracnsactionid = models.CharField(db_column='Tracker_tracnsactionID', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subscription_mandate = models.CharField(db_column='Subscription_mandate', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subscription_paytype = models.CharField(db_column='Subscription_Paytype', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subscription_guid = models.CharField(db_column='Subscription_guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    promotioncreditid = models.IntegerField(db_column='PromotionCreditID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscriptionuserdetails'


class Subscriptionuserwisepayment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usersubscriptionid = models.IntegerField(db_column='UsersubscriptionId', blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='Paymentdate', blank=True, null=True)  # Field name made lowercase.
    mobilecharges = models.DecimalField(db_column='Mobilecharges', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentammount = models.DecimalField(db_column='Paymentammount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subscriptionpcakage = models.CharField(db_column='Subscriptionpcakage', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    paymentinterval = models.CharField(db_column='PaymentInterval', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptionuserwisepayment'


class TblAdminformssection(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    filepath = models.CharField(db_column='Filepath', max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_adminformssection'


class TblCustomerreviewratting(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='Phonenumber', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    rate_star = models.IntegerField(db_column='Rate_star', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='Shortdescription', max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    isdisplay = models.IntegerField(db_column='Isdisplay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_customerreviewratting'


class TblDistanceradiousmaster(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='Postalcode', max_length=20, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    postalcode_latitude = models.FloatField(db_column='Postalcode_latitude', blank=True, null=True)  # Field name made lowercase.
    postalcode_longitide = models.FloatField(db_column='Postalcode_longitide', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_distanceradiousmaster'


class TblGeozonesettings(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    trackerid = models.FloatField(db_column='TrackerID', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    lonitude = models.FloatField(db_column='Lonitude', blank=True, null=True)  # Field name made lowercase.
    geozoneactivated = models.IntegerField(db_column='GeoZoneActivated', blank=True, null=True)  # Field name made lowercase.
    locationdatetime = models.DateTimeField(db_column='Locationdatetime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_geozonesettings'


class TblHeadercontent(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    content_1 = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    content_2 = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    registrationline1 = models.TextField(db_column='RegistrationLine1', blank=True, null=True)  # Field name made lowercase.
    registrationline2 = models.TextField(db_column='RegistrationLine2', blank=True, null=True)  # Field name made lowercase.
    headercontent1 = models.TextField(db_column='HeaderContent1', blank=True, null=True)  # Field name made lowercase.
    headercontent2 = models.TextField(db_column='HeaderContent2', blank=True, null=True)  # Field name made lowercase.
    headercontent3 = models.TextField(db_column='HeaderContent3', blank=True, null=True)  # Field name made lowercase.
    dealercontent = models.TextField(db_column='DealerContent', blank=True, null=True)  # Field name made lowercase.
    headerregisterpart1 = models.TextField(db_column='HeaderRegisterPart1', blank=True, null=True)  # Field name made lowercase.
    headerregisterpart2 = models.TextField(db_column='HeaderRegisterPart2', blank=True, null=True)  # Field name made lowercase.
    headerregisterpart3 = models.TextField(db_column='HeaderRegisterPart3', blank=True, null=True)  # Field name made lowercase.
    purchasepackagedetails = models.TextField(db_column='PurchasePackageDetails', blank=True, null=True)  # Field name made lowercase.
    jobcontentdetails = models.TextField(db_column='JobContentDetails', blank=True, null=True)  # Field name made lowercase.
    footertrackcontent = models.TextField(db_column='FooterTrackContent', blank=True, null=True)  # Field name made lowercase.
    footertrackaddress = models.TextField(db_column='FooterTrackAddress', blank=True, null=True)  # Field name made lowercase.
    footertrackcontent2 = models.TextField(db_column='FooterTrackContent2', blank=True, null=True)  # Field name made lowercase.
    termsofservice = models.TextField(db_column='TermsOfService', blank=True, null=True)  # Field name made lowercase.
    privacypolicy = models.TextField(db_column='PrivacyPolicy', blank=True, null=True)  # Field name made lowercase.
    imprint = models.TextField(db_column='Imprint', blank=True, null=True)  # Field name made lowercase.
    shopcontentproduct1 = models.TextField(db_column='ShopContentProduct1', blank=True, null=True)  # Field name made lowercase.
    shopcontentproduct2 = models.TextField(db_column='ShopContentProduct2', blank=True, null=True)  # Field name made lowercase.
    shopcontentproduct3 = models.TextField(db_column='ShopContentProduct3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_headercontent'


class TblInvoicetypemaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    invocietype = models.CharField(db_column='Invocietype', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_invoicetypemaster'


class TblIpnresponse(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    strrequest = models.TextField(db_column='strRequest', blank=True, null=True)  # Field name made lowercase.
    verificationresponse = models.TextField(db_column='verificationResponse', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ipnresponse'


class TblLat(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lat = models.TextField(blank=True, null=True)
    long = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_lat'


class TblLocationstorage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    trackerid = models.FloatField(db_column='TrackerID', blank=True, null=True)  # Field name made lowercase.
    location_date = models.CharField(db_column='Location_Date', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    location_time = models.CharField(db_column='Location_time', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    lonitude = models.FloatField(db_column='Lonitude', blank=True, null=True)  # Field name made lowercase.
    speed = models.FloatField(db_column='Speed', blank=True, null=True)  # Field name made lowercase.
    locationdatetime = models.DateTimeField(db_column='Locationdatetime', blank=True, null=True)  # Field name made lowercase.
    locationstring = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_locationstorage'


class TblMobilecardcharges(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    mobilecardcharges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_mobilecardcharges'


class TblRadiousmaster(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    radious = models.IntegerField(blank=True, null=True)
    parameter = models.CharField(max_length=10, db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_radiousmaster'


class TblTempsubscriptiongocardlessdata(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    salutation = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(db_column='Firstname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    datebirth = models.CharField(db_column='Datebirth', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    regemail = models.CharField(db_column='RegEmail', max_length=256, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    regphoneno = models.CharField(db_column='RegPhoneno', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='Postalcode', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    road = models.CharField(db_column='Road', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    acquiredby = models.CharField(db_column='Acquiredby', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subscriptiontype = models.IntegerField(db_column='Subscriptiontype', blank=True, null=True)  # Field name made lowercase.
    payment_interval = models.IntegerField(db_column='Payment_Interval', blank=True, null=True)  # Field name made lowercase.
    tracker_type = models.IntegerField(db_column='Tracker_Type', blank=True, null=True)  # Field name made lowercase.
    redirectflow_id = models.CharField(db_column='redirectFlow_ID', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    redirecturl = models.CharField(db_column='RedirectUrl', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    subscriptionguid = models.CharField(db_column='Subscriptionguid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    subscription_userdetailsid = models.IntegerField(db_column='subscription_userdetailsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_tempsubscriptiongocardlessdata'


class TblTestlocationdata(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    locationdetails = models.TextField(db_column='Locationdetails', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_testlocationdata'


class TblTrackeralarmresponse(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    trackeralarmresponse = models.CharField(db_column='Trackeralarmresponse', max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_trackeralarmresponse'


class TblTrackerresponse(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_trackerresponse'


class TblTrackervehicleresponselog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='VehicleID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(blank=True, null=True)
    alarmtype = models.CharField(db_column='AlarmType', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_trackervehicleresponselog'


class TblVehiclesubscriptioncharges(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    subscriptionid = models.IntegerField(blank=True, null=True)
    vehiclecharges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mobilecharges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paymentinterval = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_vehiclesubscriptioncharges'


class TrackerQtymanagement(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    trackerid = models.IntegerField(db_column='TrackerId', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='Updatedon', blank=True, null=True)  # Field name made lowercase.
    added_qty = models.IntegerField(db_column='Added_qty', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='Createdby', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tracker_qtymanagement'


class Trackeralarms(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    trackerid = models.FloatField(db_column='TrackerID', blank=True, null=True)  # Field name made lowercase.
    location_date = models.CharField(db_column='Location_Date', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    location_time = models.CharField(db_column='Location_time', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    command = models.CharField(db_column='Command', max_length=100, blank=True, null=True)  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=100, blank=True, null=True)  # Field name made lowercase.
    commandstatus = models.CharField(db_column='CommandStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    locationdatetime = models.DateTimeField(db_column='Locationdatetime', blank=True, null=True)  # Field name made lowercase.
    alarmtrigger = models.IntegerField(db_column='AlarmTrigger', blank=True, null=True)  # Field name made lowercase.
    alarmtype = models.CharField(db_column='AlarmType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat', blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(db_column='Long', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trackeralarms'


class Trackercategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tracker_category = models.CharField(db_column='Tracker_Category', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='Isactive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trackercategory'


class Trackeritemimages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    trackerid = models.IntegerField(db_column='TrackerId', blank=True, null=True)  # Field name made lowercase.
    imagename = models.CharField(db_column='Imagename', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trackeritemimages'


class Trackerlisitem(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    trackername = models.CharField(db_column='Trackername', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    trackercategory = models.IntegerField(db_column='TrackerCategory', blank=True, null=True)  # Field name made lowercase.
    trackershortdesc = models.CharField(db_column='Trackershortdesc', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dicountprice = models.DecimalField(db_column='DicountPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    original_qty = models.IntegerField(db_column='Original_qty', blank=True, null=True)  # Field name made lowercase.
    pending_qty = models.IntegerField(db_column='Pending_qty', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='Isactive', blank=True, null=True)  # Field name made lowercase.
    articlenumber = models.IntegerField(db_column='Articlenumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trackerlisitem'


class Trackerlist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    trackername = models.CharField(db_column='TrackerName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trackername_german = models.CharField(db_column='TrackerName_german', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trackerdesc = models.CharField(db_column='Trackerdesc', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trackerdesc_german = models.CharField(db_column='Trackerdesc_german', max_length=500, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    price_german = models.DecimalField(db_column='Price_german', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountprice = models.DecimalField(db_column='Discountprice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountprice_german = models.DecimalField(db_column='Discountprice_german', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trackerlist'


class Trackerorderitems(models.Model):
    orderitemid = models.IntegerField(db_column='OrderItemID', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    cartid = models.CharField(db_column='CartID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trackercategoryid = models.IntegerField(db_column='TrackerCategoryId', blank=True, null=True)  # Field name made lowercase.
    trackercategory = models.CharField(db_column='TrackerCategory', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    trackerid = models.IntegerField(db_column='TrackerId', blank=True, null=True)  # Field name made lowercase.
    trackername = models.CharField(db_column='TrackerName', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    trackerimage = models.CharField(db_column='TrackerImage', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    articleno = models.IntegerField(db_column='ArticleNo', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='Unitprice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quentity = models.IntegerField(db_column='Quentity', blank=True, null=True)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='Totalprice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    subscriptionid = models.IntegerField(db_column='SubscriptionId', blank=True, null=True)  # Field name made lowercase.
    subscriptionname = models.CharField(db_column='SubscriptionName', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subscriptionpaymenttype = models.IntegerField(db_column='SubscriptionPaymentType', blank=True, null=True)  # Field name made lowercase.
    subscriptionpaymentname = models.CharField(db_column='subscriptionPaymentname', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subscriptionuserdetails_id = models.IntegerField(db_column='SubscriptionUserdetails_ID', blank=True, null=True)  # Field name made lowercase.
    invoicenote = models.CharField(db_column='Invoicenote', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
    vehiclename = models.CharField(db_column='Vehiclename', max_length=200, blank=True, null=True)  # Field name made lowercase.
    vehicle_licence_plate = models.CharField(db_column='Vehicle_Licence_Plate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vehiclecharges = models.DecimalField(db_column='VehicleCharges', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mobilecharges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vehicle_paytype = models.CharField(db_column='Vehicle_Paytype', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mobile_paytype = models.CharField(db_column='Mobile_Paytype', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tracker_price = models.DecimalField(db_column='Tracker_price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tracker_activationfees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trackerorderitems'


class Trackerorderpaymenttypemaster(models.Model):
    paytypeid = models.IntegerField(db_column='Paytypeid', blank=True, null=True)  # Field name made lowercase.
    paytypename = models.CharField(db_column='Paytypename', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trackerorderpaymenttypemaster'


class Trackerorders(models.Model):
    orderid = models.IntegerField(db_column='OrderId', blank=True, null=True)  # Field name made lowercase.
    cartid = models.CharField(db_column='CartId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orderguid = models.CharField(db_column='OrderGUID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=256, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='Userfullname', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    sid = models.IntegerField(blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)
    shippingaddress = models.CharField(db_column='Shippingaddress', max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='Billingaddress', max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='Subtotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    shippingcharges = models.DecimalField(db_column='Shippingcharges', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='Grandtotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='Paymenttype', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    isfail = models.IntegerField(db_column='Isfail', blank=True, null=True)  # Field name made lowercase.
    orderstatusid = models.IntegerField(db_column='OrderstatusId', blank=True, null=True)  # Field name made lowercase.
    paypal_txtid = models.CharField(db_column='Paypal_txtid', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    stripecharge_id = models.CharField(db_column='stripeCharge_Id', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    invoicetype = models.IntegerField(db_column='InvoiceType', blank=True, null=True)  # Field name made lowercase.
    subscriptionuserdetails_id = models.IntegerField(db_column='SubscriptionUserdetails_ID', blank=True, null=True)  # Field name made lowercase.
    vehicle_id = models.IntegerField(db_column='Vehicle_ID', blank=True, null=True)  # Field name made lowercase.
    redirectflow_gocardlessid = models.CharField(db_column='Redirectflow_GocardlessID', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trackerorders'


class Trackerorderstatusmaster(models.Model):
    orderstatusid = models.IntegerField(db_column='OrderstatusId', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='Orderstatus', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trackerorderstatusmaster'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    salutation = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(db_column='Firstname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    responsibleforcampingplaceid = models.IntegerField(db_column='ResponsibleForCampingPlaceId', blank=True, null=True)  # Field name made lowercase.
    address_city = models.CharField(db_column='Address_City', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_country = models.CharField(db_column='Address_Country', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_street = models.CharField(db_column='Address_Street', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_postal = models.CharField(db_column='Address_Postal', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_state = models.CharField(db_column='Address_State', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    address_latitude = models.FloatField(db_column='Address_Latitude', blank=True, null=True)  # Field name made lowercase.
    address_longitude = models.FloatField(db_column='Address_Longitude', blank=True, null=True)  # Field name made lowercase.
    creadtedby = models.CharField(db_column='Creadtedby', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='Createdon', blank=True, null=True)  # Field name made lowercase.
    lastupdatedon = models.DateTimeField(db_column='LastUpdatedon', blank=True, null=True)  # Field name made lowercase.
    newslettersubscribe = models.IntegerField(db_column='NewsLetterSubscribe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class UsersMerchantemployee(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    merchantid = models.IntegerField(db_column='MerchantId', blank=True, null=True)  # Field name made lowercase.
    paypalid = models.CharField(db_column='PayPalId', max_length=500, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_merchantemployee'


class Usersubcriptionpackagedetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subscriptionuserid = models.IntegerField(db_column='SubscriptionuserId', blank=True, null=True)  # Field name made lowercase.
    packagename = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    packagename_german = models.CharField(max_length=200, db_collation='utf8_general_ci', blank=True, null=True)
    extractingreadingthedata = models.IntegerField(db_column='Extractingreadingthedata', blank=True, null=True)  # Field name made lowercase.
    realtimemonitoring = models.IntegerField(db_column='Realtimemonitoring', blank=True, null=True)  # Field name made lowercase.
    livetracking = models.IntegerField(db_column='Livetracking', blank=True, null=True)  # Field name made lowercase.
    dealersearchinyourarea = models.IntegerField(db_column='Dealersearchinyourarea', blank=True, null=True)  # Field name made lowercase.
    alarmonpresssosbutton = models.IntegerField(db_column='AlarmonPressSOSbutton', blank=True, null=True)  # Field name made lowercase.
    alarmonoverspeed = models.IntegerField(db_column='Alarmonoverspeed', blank=True, null=True)  # Field name made lowercase.
    alarmatvibration = models.IntegerField(db_column='Alarmatvibration', blank=True, null=True)  # Field name made lowercase.
    alarmonleavinganarea_geofence = models.IntegerField(db_column='Alarmonleavinganarea_geofence', blank=True, null=True)  # Field name made lowercase.
    holidaymode_vehiclecannotbemonitoredonholidayifdesired = models.IntegerField(db_column='Holidaymode_vehiclecannotbemonitoredonholidayifdesired', blank=True, null=True)  # Field name made lowercase.
    falsealarmincluded_beforevehiclemoved_mustswitchedoff = models.IntegerField(db_column='Falsealarmincluded_beforevehiclemoved_mustswitchedoff', blank=True, null=True)  # Field name made lowercase.
    locationqueryperday = models.IntegerField(db_column='Locationqueryperday', blank=True, null=True)  # Field name made lowercase.
    archivehistoryofvehiclelocations = models.CharField(db_column='Archivehistoryofvehiclelocations', max_length=100, blank=True, null=True)  # Field name made lowercase.
    immediatereplacementserviceofthetracker = models.CharField(db_column='Immediatereplacementserviceofthetracker', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vehiclefleetmanagement_numberofvehicles = models.IntegerField(db_column='Vehiclefleetmanagement_numberofvehicles', blank=True, null=True)  # Field name made lowercase.
    support_service_starttime = models.CharField(db_column='Support_Service_StartTime', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    support_service_endtime = models.CharField(db_column='Support_Service_EndTime', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    bringbackservice = models.CharField(db_column='BringBackService', max_length=100, blank=True, null=True)  # Field name made lowercase.
    activationfeeoncepervehicle = models.DecimalField(db_column='Activationfeeoncepervehicle', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    annualpricepervehicle = models.DecimalField(db_column='Annualpricepervehicle', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mobilesimcardincl_dataroamingeumtl = models.DecimalField(db_column='MobileSIMcardincl_DataroamingEUmtl', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isallowpayment = models.IntegerField(db_column='Isallowpayment', blank=True, null=True)  # Field name made lowercase.
    pricemonthly = models.DecimalField(db_column='PriceMonthly', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricequarter = models.DecimalField(db_column='PriceQuarter', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricehalf = models.DecimalField(db_column='PriceHalf', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priceoneyear = models.DecimalField(db_column='PriceOneYear', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricetwoyear = models.DecimalField(db_column='PriceTwoYear', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bringbackservicefrom = models.CharField(db_column='BringBackServiceFrom', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    bringbackserviceup = models.CharField(db_column='BringBackServiceUp', max_length=16, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='Isactive', blank=True, null=True)  # Field name made lowercase.
    noofvehicleallow = models.IntegerField(db_column='Noofvehicleallow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usersubcriptionpackagedetail'


class Vehicleimages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='VehicleId', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicleimages'


class Vehicleset(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicletype = models.IntegerField(db_column='VehicleType', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    licenseplate = models.CharField(db_column='LicensePlate', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    buildingyear = models.IntegerField(db_column='BuildingYear', blank=True, null=True)  # Field name made lowercase.
    insucrencecompany = models.CharField(db_column='InsucrenceCompany', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    insurencenumber = models.CharField(db_column='InsurenceNumber', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    modeltypename = models.CharField(db_column='ModelTypeName', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    awning_type = models.CharField(db_column='Awning_Type', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    awning_brand = models.CharField(db_column='Awning_Brand', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    awning_length = models.FloatField(db_column='Awning_Length', blank=True, null=True)  # Field name made lowercase.
    solarsystem_numberofcells = models.IntegerField(db_column='SolarSystem_NumberOfCells', blank=True, null=True)  # Field name made lowercase.
    imageid = models.IntegerField(db_column='ImageId', blank=True, null=True)  # Field name made lowercase.
    bicyclerackondrawbar_brand = models.TextField(db_column='BicycleRackOnDrawbar_Brand', blank=True, null=True)  # Field name made lowercase.
    bicyclerackondrawbar_model = models.TextField(db_column='BicycleRackOnDrawbar_Model', blank=True, null=True)  # Field name made lowercase.
    bicyclerackondrawbar_number = models.IntegerField(db_column='BicycleRackOnDrawbar_Number', blank=True, null=True)  # Field name made lowercase.
    bicyclerackonstern_brand = models.TextField(db_column='BicycleRackOnStern_Brand', blank=True, null=True)  # Field name made lowercase.
    bicyclerackonstern_model = models.TextField(db_column='BicycleRackOnStern_Model', blank=True, null=True)  # Field name made lowercase.
    bicyclerackonstern_number = models.IntegerField(db_column='BicycleRackOnStern_Number', blank=True, null=True)  # Field name made lowercase.
    motorcyclecarrieronrear_brand = models.TextField(db_column='MotorcycleCarrierOnRear_Brand', blank=True, null=True)  # Field name made lowercase.
    motorcyclecarrieronrear_model = models.TextField(db_column='MotorcycleCarrierOnRear_Model', blank=True, null=True)  # Field name made lowercase.
    motorcycleormotorcycleatrear_brand = models.TextField(db_column='MotorcycleOrMotorcycleAtRear_Brand', blank=True, null=True)  # Field name made lowercase.
    motorcycleormotorcycleatrear_model = models.TextField(db_column='MotorcycleOrMotorcycleAtRear_Model', blank=True, null=True)  # Field name made lowercase.
    motorcycleormotorcycleatrear_plate = models.TextField(db_column='MotorcycleOrMotorcycleAtRear_Plate', blank=True, null=True)  # Field name made lowercase.
    motorcycleormotorcycleatrear_color = models.TextField(db_column='MotorcycleOrMotorcycleAtRear_Color', blank=True, null=True)  # Field name made lowercase.
    mover_brand = models.TextField(db_column='Mover_Brand', blank=True, null=True)  # Field name made lowercase.
    mover_model = models.TextField(db_column='Mover_Model', blank=True, null=True)  # Field name made lowercase.
    rooftopairconditioning_brand = models.TextField(db_column='RooftopAirConditioning_Brand', blank=True, null=True)  # Field name made lowercase.
    rooftopairconditioning_model = models.TextField(db_column='RooftopAirConditioning_Model', blank=True, null=True)  # Field name made lowercase.
    satelitesystem_brand = models.TextField(db_column='SateliteSystem_Brand', blank=True, null=True)  # Field name made lowercase.
    satelitesystem_model = models.TextField(db_column='SateliteSystem_Model', blank=True, null=True)  # Field name made lowercase.
    size_width = models.IntegerField(db_column='Size_Width', blank=True, null=True)  # Field name made lowercase.
    size_height = models.IntegerField(db_column='Size_Height', blank=True, null=True)  # Field name made lowercase.
    size_length = models.IntegerField(db_column='Size_Length', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='Createdby', max_length=128, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    trackerid = models.FloatField(db_column='TrackerId', blank=True, null=True)  # Field name made lowercase.
    iconimage = models.CharField(db_column='IconImage', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    ispay = models.IntegerField(db_column='Ispay', blank=True, null=True)  # Field name made lowercase.
    subscription_id = models.IntegerField(db_column='Subscription_ID', blank=True, null=True)  # Field name made lowercase.
    payment_subscriptionpayid = models.CharField(db_column='Payment_subscriptionPayID', max_length=150, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    istrackerconfiguration = models.IntegerField(db_column='Istrackerconfiguration', blank=True, null=True)  # Field name made lowercase.
    tracker_mobilenumber = models.CharField(db_column='Tracker_mobilenumber', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    tracker_mobile_apn = models.CharField(db_column='Tracker_mobile_apn', max_length=50, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    iscentralnumberconfiguration = models.IntegerField(db_column='Iscentralnumberconfiguration', blank=True, null=True)  # Field name made lowercase.
    isgeofanceactive = models.IntegerField(db_column='Isgeofanceactive', blank=True, null=True)  # Field name made lowercase.
    isoverspeedactive = models.IntegerField(db_column='Isoverspeedactive', blank=True, null=True)  # Field name made lowercase.
    isvibrationactive = models.IntegerField(db_column='Isvibrationactive', blank=True, null=True)  # Field name made lowercase.
    islowbatteryactive = models.IntegerField(db_column='Islowbatteryactive', blank=True, null=True)  # Field name made lowercase.
    ispoweroffactive = models.IntegerField(db_column='Ispoweroffactive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicleset'


class Vehicletypemaster(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicletype = models.CharField(db_column='VehicleType', max_length=100, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicletypemaster'


class Websitegraphics(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    banner_image1 = models.TextField(db_column='Banner_Image1', blank=True, null=True)  # Field name made lowercase.
    banner_image2 = models.TextField(db_column='Banner_Image2', blank=True, null=True)  # Field name made lowercase.
    banner_image3 = models.TextField(db_column='Banner_Image3', blank=True, null=True)  # Field name made lowercase.
    product_image1 = models.TextField(db_column='Product_Image1', blank=True, null=True)  # Field name made lowercase.
    product_image2 = models.TextField(db_column='Product_Image2', blank=True, null=True)  # Field name made lowercase.
    product_image3 = models.TextField(db_column='Product_Image3', blank=True, null=True)  # Field name made lowercase.
    shop_background_image = models.TextField(db_column='Shop_Background_Image', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'websitegraphics'
