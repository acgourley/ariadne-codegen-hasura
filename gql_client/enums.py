# Generated by ariadne-codegen
# Source: http://localhost:8080/v1/graphql

from enum import Enum


class AccountsConstraint(str, Enum):
    accounts_pkey = "accounts_pkey"


class AccountsSelectColumn(str, Enum):
    accessToken = "accessToken"
    expiresAt = "expiresAt"
    id = "id"
    idToken = "idToken"
    provider = "provider"
    providerAccountId = "providerAccountId"
    refreshToken = "refreshToken"
    scope = "scope"
    sessionState = "sessionState"
    tokenType = "tokenType"
    type = "type"
    userId = "userId"


class AccountsUpdateColumn(str, Enum):
    accessToken = "accessToken"
    expiresAt = "expiresAt"
    id = "id"
    idToken = "idToken"
    provider = "provider"
    providerAccountId = "providerAccountId"
    refreshToken = "refreshToken"
    scope = "scope"
    sessionState = "sessionState"
    tokenType = "tokenType"
    type = "type"
    userId = "userId"


class AuthenticatorConstraint(str, Enum):
    Authenticator_credentialID_key = "Authenticator_credentialID_key"
    Authenticator_pkey = "Authenticator_pkey"


class AuthenticatorSelectColumn(str, Enum):
    counter = "counter"
    credentialBackedUp = "credentialBackedUp"
    credentialDeviceType = "credentialDeviceType"
    credentialID = "credentialID"
    credentialPublicKey = "credentialPublicKey"
    id = "id"
    providerAccountId = "providerAccountId"
    transports = "transports"
    userId = "userId"


class AuthenticatorUpdateColumn(str, Enum):
    counter = "counter"
    credentialBackedUp = "credentialBackedUp"
    credentialDeviceType = "credentialDeviceType"
    credentialID = "credentialID"
    credentialPublicKey = "credentialPublicKey"
    id = "id"
    providerAccountId = "providerAccountId"
    transports = "transports"
    userId = "userId"


class BallotItemsConstraint(str, Enum):
    ballot_items_measure_id_key = "ballot_items_measure_id_key"
    ballot_items_pkey = "ballot_items_pkey"
    ballot_items_race_id_key = "ballot_items_race_id_key"


class BallotItemsSelectColumn(str, Enum):
    ballotOrder = "ballotOrder"
    createdAt = "createdAt"
    electionId = "electionId"
    id = "id"
    measureId = "measureId"
    raceId = "raceId"
    updatedAt = "updatedAt"


class BallotItemsUpdateColumn(str, Enum):
    ballotOrder = "ballotOrder"
    createdAt = "createdAt"
    electionId = "electionId"
    id = "id"
    measureId = "measureId"
    raceId = "raceId"
    updatedAt = "updatedAt"


class BrandsConstraint(str, Enum):
    brands_pkey = "brands_pkey"


class BrandsSelectColumn(str, Enum):
    createdAt = "createdAt"
    description = "description"
    headerImageId = "headerImageId"
    id = "id"
    logoImageId = "logoImageId"
    name = "name"
    parentBrandId = "parentBrandId"
    shortDescription = "shortDescription"
    type = "type"
    updatedAt = "updatedAt"


class BrandsUpdateColumn(str, Enum):
    createdAt = "createdAt"
    description = "description"
    headerImageId = "headerImageId"
    id = "id"
    logoImageId = "logoImageId"
    name = "name"
    parentBrandId = "parentBrandId"
    shortDescription = "shortDescription"
    type = "type"
    updatedAt = "updatedAt"


class CandidaciesConstraint(str, Enum):
    candidacies_pkey = "candidacies_pkey"


class CandidaciesSelectColumn(str, Enum):
    campaignUrlId = "campaignUrlId"
    createdAt = "createdAt"
    id = "id"
    infoUrlId = "infoUrlId"
    partyId = "partyId"
    personId = "personId"
    raceId = "raceId"
    updatedAt = "updatedAt"


class CandidaciesUpdateColumn(str, Enum):
    campaignUrlId = "campaignUrlId"
    createdAt = "createdAt"
    id = "id"
    infoUrlId = "infoUrlId"
    partyId = "partyId"
    personId = "personId"
    raceId = "raceId"
    updatedAt = "updatedAt"


class CursorOrdering(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


class ElectionsConstraint(str, Enum):
    elections_pkey = "elections_pkey"


class ElectionsSelectColumn(str, Enum):
    createdAt = "createdAt"
    date = "date"
    id = "id"
    name = "name"
    ocdId = "ocdId"
    updatedAt = "updatedAt"


class ElectionsUpdateColumn(str, Enum):
    createdAt = "createdAt"
    date = "date"
    id = "id"
    name = "name"
    ocdId = "ocdId"
    updatedAt = "updatedAt"


class GroupBrandRelationshipTypesConstraint(str, Enum):
    group_brand_relationship_types_pkey = "group_brand_relationship_types_pkey"


class GroupBrandRelationshipTypesEnum(str, Enum):
    OWNER = "OWNER"
    VIEWER = "VIEWER"


class GroupBrandRelationshipTypesSelectColumn(str, Enum):
    description = "description"
    value = "value"


class GroupBrandRelationshipTypesUpdateColumn(str, Enum):
    description = "description"
    value = "value"


class GroupBrandRelationshipsConstraint(str, Enum):
    group_brand_relationships_group_id_brand_id_type_key = (
        "group_brand_relationships_group_id_brand_id_type_key"
    )
    group_brand_relationships_pkey = "group_brand_relationships_pkey"


class GroupBrandRelationshipsSelectColumn(str, Enum):
    brandId = "brandId"
    createdAt = "createdAt"
    groupId = "groupId"
    id = "id"
    type = "type"
    updatedAt = "updatedAt"


class GroupBrandRelationshipsUpdateColumn(str, Enum):
    brandId = "brandId"
    createdAt = "createdAt"
    groupId = "groupId"
    id = "id"
    type = "type"
    updatedAt = "updatedAt"


class GroupPersonRelationshipTypesConstraint(str, Enum):
    group_person_relationship_types_pkey = "group_person_relationship_types_pkey"


class GroupPersonRelationshipTypesEnum(str, Enum):
    VIEWER = "VIEWER"


class GroupPersonRelationshipTypesSelectColumn(str, Enum):
    description = "description"
    value = "value"


class GroupPersonRelationshipTypesUpdateColumn(str, Enum):
    description = "description"
    value = "value"


class GroupPersonRelationshipsConstraint(str, Enum):
    group_person_relationships_group_id_person_id_type_key = (
        "group_person_relationships_group_id_person_id_type_key"
    )
    group_person_relationships_pkey = "group_person_relationships_pkey"


class GroupPersonRelationshipsSelectColumn(str, Enum):
    createdAt = "createdAt"
    groupId = "groupId"
    id = "id"
    personId = "personId"
    type = "type"
    updatedAt = "updatedAt"


class GroupPersonRelationshipsUpdateColumn(str, Enum):
    createdAt = "createdAt"
    groupId = "groupId"
    id = "id"
    personId = "personId"
    type = "type"
    updatedAt = "updatedAt"


class GroupTypesConstraint(str, Enum):
    group_types_pkey = "group_types_pkey"


class GroupTypesEnum(str, Enum):
    PUBLIC = "PUBLIC"
    SELF = "SELF"


class GroupTypesSelectColumn(str, Enum):
    description = "description"
    value = "value"


class GroupTypesUpdateColumn(str, Enum):
    description = "description"
    value = "value"


class GroupsConstraint(str, Enum):
    group_public_unique_key = "group_public_unique_key"
    groups_pkey = "groups_pkey"


class GroupsSelectColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    isExclusionary = "isExclusionary"
    name = "name"
    type = "type"
    updatedAt = "updatedAt"


class GroupsUpdateColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    isExclusionary = "isExclusionary"
    name = "name"
    type = "type"
    updatedAt = "updatedAt"


class GuidesConstraint(str, Enum):
    guides_brand_id_election_id_key = "guides_brand_id_election_id_key"
    guides_pkey = "guides_pkey"


class GuidesSelectColumn(str, Enum):
    brandId = "brandId"
    createdAt = "createdAt"
    description = "description"
    electionId = "electionId"
    id = "id"
    isDiscoverable = "isDiscoverable"
    updatedAt = "updatedAt"


class GuidesSelectColumnGuidesAggregateBoolExpBool_andArgumentsColumns(str, Enum):
    isDiscoverable = "isDiscoverable"


class GuidesSelectColumnGuidesAggregateBoolExpBool_orArgumentsColumns(str, Enum):
    isDiscoverable = "isDiscoverable"


class GuidesUpdateColumn(str, Enum):
    brandId = "brandId"
    createdAt = "createdAt"
    description = "description"
    electionId = "electionId"
    id = "id"
    isDiscoverable = "isDiscoverable"
    updatedAt = "updatedAt"


class ImagesConstraint(str, Enum):
    images_pkey = "images_pkey"


class ImagesSelectColumn(str, Enum):
    blurDataUrl = "blurDataUrl"
    createdAt = "createdAt"
    description = "description"
    height = "height"
    id = "id"
    name = "name"
    sourceUrlId = "sourceUrlId"
    updatedAt = "updatedAt"
    width = "width"


class ImagesUpdateColumn(str, Enum):
    blurDataUrl = "blurDataUrl"
    createdAt = "createdAt"
    description = "description"
    height = "height"
    id = "id"
    name = "name"
    sourceUrlId = "sourceUrlId"
    updatedAt = "updatedAt"
    width = "width"


class LevelsConstraint(str, Enum):
    levels_pkey = "levels_pkey"


class LevelsEnum(str, Enum):
    CITY = "CITY"
    COUNTY = "COUNTY"
    FEDERAL = "FEDERAL"
    LOCAL = "LOCAL"
    REGIONAL = "REGIONAL"
    STATE = "STATE"
    TOWNSHIP = "TOWNSHIP"


class LevelsSelectColumn(str, Enum):
    description = "description"
    value = "value"


class LevelsUpdateColumn(str, Enum):
    description = "description"
    value = "value"


class MeasuresConstraint(str, Enum):
    measures_pkey = "measures_pkey"


class MeasuresSelectColumn(str, Enum):
    conSnippet = "conSnippet"
    createdAt = "createdAt"
    id = "id"
    legalText = "legalText"
    level = "level"
    name = "name"
    passageThreshold = "passageThreshold"
    proSnippet = "proSnippet"
    summary = "summary"
    title = "title"
    updatedAt = "updatedAt"


class MeasuresUpdateColumn(str, Enum):
    conSnippet = "conSnippet"
    createdAt = "createdAt"
    id = "id"
    legalText = "legalText"
    level = "level"
    name = "name"
    passageThreshold = "passageThreshold"
    proSnippet = "proSnippet"
    summary = "summary"
    title = "title"
    updatedAt = "updatedAt"


class OrderBy(str, Enum):
    ASC = "ASC"
    ASC_NULLS_FIRST = "ASC_NULLS_FIRST"
    ASC_NULLS_LAST = "ASC_NULLS_LAST"
    DESC = "DESC"
    DESC_NULLS_FIRST = "DESC_NULLS_FIRST"
    DESC_NULLS_LAST = "DESC_NULLS_LAST"


class PartiesConstraint(str, Enum):
    parties_pkey = "parties_pkey"


class PartiesSelectColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    name = "name"
    shortName = "shortName"
    updatedAt = "updatedAt"


class PartiesUpdateColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    name = "name"
    shortName = "shortName"
    updatedAt = "updatedAt"


class PersonGroupRelationshipTypesConstraint(str, Enum):
    person_group_relationship_types_pkey = "person_group_relationship_types_pkey"


class PersonGroupRelationshipTypesEnum(str, Enum):
    MEMBER = "MEMBER"
    OWNER = "OWNER"
    SELF = "SELF"
    VIEWER = "VIEWER"


class PersonGroupRelationshipTypesSelectColumn(str, Enum):
    description = "description"
    value = "value"


class PersonGroupRelationshipTypesUpdateColumn(str, Enum):
    description = "description"
    value = "value"


class PersonGroupRelationshipsConstraint(str, Enum):
    person_group_relationships_pkey = "person_group_relationships_pkey"


class PersonGroupRelationshipsSelectColumn(str, Enum):
    createdAt = "createdAt"
    groupId = "groupId"
    id = "id"
    personId = "personId"
    type = "type"
    updatedAt = "updatedAt"


class PersonGroupRelationshipsUpdateColumn(str, Enum):
    createdAt = "createdAt"
    groupId = "groupId"
    id = "id"
    personId = "personId"
    type = "type"
    updatedAt = "updatedAt"


class PersonsConstraint(str, Enum):
    persons_brand_id_key = "persons_brand_id_key"
    persons_pkey = "persons_pkey"


class PersonsSelectColumn(str, Enum):
    brandId = "brandId"
    createdAt = "createdAt"
    fullName = "fullName"
    headshotImageId = "headshotImageId"
    id = "id"
    updatedAt = "updatedAt"


class PersonsUpdateColumn(str, Enum):
    brandId = "brandId"
    createdAt = "createdAt"
    fullName = "fullName"
    headshotImageId = "headshotImageId"
    id = "id"
    updatedAt = "updatedAt"


class PositionsConstraint(str, Enum):
    positions_pkey = "positions_pkey"


class PositionsSelectColumn(str, Enum):
    createdAt = "createdAt"
    description = "description"
    geoId = "geoId"
    hasRankedChoiceGeneral = "hasRankedChoiceGeneral"
    hasRankedChoicePrimary = "hasRankedChoicePrimary"
    id = "id"
    level = "level"
    name = "name"
    numSeats = "numSeats"
    ocdId = "ocdId"
    updatedAt = "updatedAt"


class PositionsUpdateColumn(str, Enum):
    createdAt = "createdAt"
    description = "description"
    geoId = "geoId"
    hasRankedChoiceGeneral = "hasRankedChoiceGeneral"
    hasRankedChoicePrimary = "hasRankedChoicePrimary"
    id = "id"
    level = "level"
    name = "name"
    numSeats = "numSeats"
    ocdId = "ocdId"
    updatedAt = "updatedAt"


class ProviderTypeConstraint(str, Enum):
    provider_type_pkey = "provider_type_pkey"


class ProviderTypeSelectColumn(str, Enum):
    value = "value"


class ProviderTypeUpdateColumn(str, Enum):
    value = "value"


class RaceRaceRelationshipTypesConstraint(str, Enum):
    race_race_relationship_types_pkey = "race_race_relationship_types_pkey"


class RaceRaceRelationshipTypesEnum(str, Enum):
    IS_PRIMARY_FOR = "IS_PRIMARY_FOR"
    IS_RUNOFF_FOR = "IS_RUNOFF_FOR"


class RaceRaceRelationshipTypesSelectColumn(str, Enum):
    description = "description"
    value = "value"


class RaceRaceRelationshipTypesUpdateColumn(str, Enum):
    description = "description"
    value = "value"


class RaceRaceRelationshipsConstraint(str, Enum):
    race_race_relationships_pkey = "race_race_relationships_pkey"


class RaceRaceRelationshipsSelectColumn(str, Enum):
    sourceRaceId = "sourceRaceId"
    targetRaceId = "targetRaceId"
    type = "type"


class RaceRaceRelationshipsUpdateColumn(str, Enum):
    sourceRaceId = "sourceRaceId"
    targetRaceId = "targetRaceId"
    type = "type"


class RacesConstraint(str, Enum):
    races_pkey = "races_pkey"


class RacesSelectColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    isDisabled = "isDisabled"
    isPartisan = "isPartisan"
    isRankedChoice = "isRankedChoice"
    isRecall = "isRecall"
    isUnexpired = "isUnexpired"
    name = "name"
    numSelectionsMax = "numSelectionsMax"
    positionId = "positionId"
    updatedAt = "updatedAt"


class RacesSelectColumnRacesAggregateBoolExpBool_andArgumentsColumns(str, Enum):
    isDisabled = "isDisabled"
    isPartisan = "isPartisan"
    isRankedChoice = "isRankedChoice"
    isRecall = "isRecall"
    isUnexpired = "isUnexpired"


class RacesSelectColumnRacesAggregateBoolExpBool_orArgumentsColumns(str, Enum):
    isDisabled = "isDisabled"
    isPartisan = "isPartisan"
    isRankedChoice = "isRankedChoice"
    isRecall = "isRecall"
    isUnexpired = "isUnexpired"


class RacesUpdateColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    isDisabled = "isDisabled"
    isPartisan = "isPartisan"
    isRankedChoice = "isRankedChoice"
    isRecall = "isRecall"
    isUnexpired = "isUnexpired"
    name = "name"
    numSelectionsMax = "numSelectionsMax"
    positionId = "positionId"
    updatedAt = "updatedAt"


class SelectionsConstraint(str, Enum):
    selections_pkey = "selections_pkey"
    selections_viewpoint_id_candidacy_id_key = (
        "selections_viewpoint_id_candidacy_id_key"
    )


class SelectionsSelectColumn(str, Enum):
    candidacyId = "candidacyId"
    createdAt = "createdAt"
    id = "id"
    note = "note"
    rank = "rank"
    updatedAt = "updatedAt"
    viewpointId = "viewpointId"
    weight = "weight"


class SelectionsUpdateColumn(str, Enum):
    candidacyId = "candidacyId"
    createdAt = "createdAt"
    id = "id"
    note = "note"
    rank = "rank"
    updatedAt = "updatedAt"
    viewpointId = "viewpointId"
    weight = "weight"


class SessionsConstraint(str, Enum):
    sessions_pkey = "sessions_pkey"


class SessionsSelectColumn(str, Enum):
    expires = "expires"
    id = "id"
    sessionToken = "sessionToken"
    userId = "userId"


class SessionsUpdateColumn(str, Enum):
    expires = "expires"
    id = "id"
    sessionToken = "sessionToken"
    userId = "userId"


class UrlsConstraint(str, Enum):
    urls_pkey = "urls_pkey"


class UrlsSelectColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    linkText = "linkText"
    type = "type"
    updatedAt = "updatedAt"
    url = "url"


class UrlsUpdateColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    linkText = "linkText"
    type = "type"
    updatedAt = "updatedAt"
    url = "url"


class UsersConstraint(str, Enum):
    users_email_key = "users_email_key"
    users_person_id_key = "users_person_id_key"
    users_pkey = "users_pkey"


class UsersSelectColumn(str, Enum):
    email = "email"
    emailVerified = "emailVerified"
    id = "id"
    image = "image"
    name = "name"
    personId = "personId"


class UsersUpdateColumn(str, Enum):
    email = "email"
    emailVerified = "emailVerified"
    id = "id"
    image = "image"
    name = "name"
    personId = "personId"


class VerificationTokensConstraint(str, Enum):
    verification_tokens_pkey = "verification_tokens_pkey"


class VerificationTokensSelectColumn(str, Enum):
    expires = "expires"
    identifier = "identifier"
    token = "token"


class VerificationTokensUpdateColumn(str, Enum):
    expires = "expires"
    identifier = "identifier"
    token = "token"


class ViewpointsConstraint(str, Enum):
    viewpoints_pkey = "viewpoints_pkey"
    viewpoints_source_guide_id_target_ballot_item_id_key = (
        "viewpoints_source_guide_id_target_ballot_item_id_key"
    )
    viewpoints_target_key = "viewpoints_target_key"


class ViewpointsSelectColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    note = "note"
    sourceGuideId = "sourceGuideId"
    targetBallotItemId = "targetBallotItemId"
    targetBrandId = "targetBrandId"
    targetGuideId = "targetGuideId"
    targetSelectionId = "targetSelectionId"
    targetViewpointId = "targetViewpointId"
    updatedAt = "updatedAt"


class ViewpointsUpdateColumn(str, Enum):
    createdAt = "createdAt"
    id = "id"
    note = "note"
    sourceGuideId = "sourceGuideId"
    targetBallotItemId = "targetBallotItemId"
    targetBrandId = "targetBrandId"
    targetGuideId = "targetGuideId"
    targetSelectionId = "targetSelectionId"
    targetViewpointId = "targetViewpointId"
    updatedAt = "updatedAt"
