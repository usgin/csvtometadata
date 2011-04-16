<xsl:stylesheet xmlns:xsl='http://www.w3.org/1999/XSL/Transform'
                version='2.0' xmlns:ns2="http://azgs.az.gov/2010/metadata/generator"
                xmlns:azgs1="http://azgs.az.gov/2010/metadata/template/v-1-2"
                xmlns:azgs2="http://azgs.az.gov/2010/metadata/source/v-1-3"
                xmlns:gmd="http://www.isotc211.org/2005/gmd"
                xmlns:gco="http://www.isotc211.org/2005/gco" xmlns:gml="http://www.opengis.net/gml"
                xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <xsl:output encoding="UTF-8" indent="yes"
                omit-xml-declaration="no"/>

    <xsl:template match="record">
        <gmd:MD_Metadata xmlns:gmd="http://www.isotc211.org/2005/gmd"
                         xmlns:gco="http://www.isotc211.org/2005/gco" xmlns:gml="http://www.opengis.net/gml"
                         xmlns:xlink="http://www.w3.org/1999/xlink"
                         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                         xsi:schemaLocation="http://www.isotc211.org/2005/gmd http://schemas.opengis.net/csw/2.0.2/profiles/apiso/1.0.0/apiso.xsd">
            <xsl:apply-templates select="metadata_uuid"/>
            <gmd:language>
                <gco:CharacterString>
                    <xsl:value-of select="metadata_language"/>
                </gco:CharacterString>
            </gmd:language>
            <gmd:characterSet>
                <gmd:MD_CharacterSetCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_CharacterSetCode" codeListValue="utf8">UTF-8</gmd:MD_CharacterSetCode>
            </gmd:characterSet>
            <xsl:apply-templates select="resource_type"/>
            <gmd:contact>
                <gmd:CI_ResponsibleParty>
                    <xsl:apply-templates select="metadata_contact_person_name"/>
                    <xsl:apply-templates select="metadata_contact_name"/>
                    <xsl:apply-templates select="metadata_contact_org_name"/>
                    <xsl:apply-templates select="metadata_contact_position_name"/>
                    <gmd:contactInfo>
                        <gmd:CI_Contact>
                            <xsl:apply-templates select="metadata_phone_fax_flag"/>
                            <gmd:address>
                                <gmd:CI_Address>
                                    <xsl:apply-templates select="metadata_contact_street_address"/>
                                    <xsl:apply-templates select="metadata_contact_city"/>
                                    <xsl:apply-templates select="metadata_contact_state"/>
                                    <xsl:apply-templates select="metadata_contact_zip"/>
                                    <gmd:country>
                                        <gco:CharacterString>USA</gco:CharacterString>
                                    </gmd:country>
                                    <gmd:electronicMailAddress>
                                        <gco:CharacterString>
                                            <xsl:value-of select="metadata_contact_email"/>
                                        </gco:CharacterString>
                                    </gmd:electronicMailAddress>
                                </gmd:CI_Address>
                            </gmd:address>
                            <xsl:apply-templates select="metadata_contact_url"/>
                        </gmd:CI_Contact>
                    </gmd:contactInfo>
                    <gmd:role>
                        <gmd:CI_RoleCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode" codeListValue="distributor">pointOfContact</gmd:CI_RoleCode>
                    </gmd:role>
                </gmd:CI_ResponsibleParty>
            </gmd:contact>
            <gmd:dateStamp>
                <gco:DateTime>
                    <xsl:value-of select="metadata_date"/>
                </gco:DateTime>
            </gmd:dateStamp>
            <gmd:metadataStandardName>
                <gco:CharacterString>ISO-USGIN</gco:CharacterString>
            </gmd:metadataStandardName>
            <gmd:metadataStandardVersion>
                <gco:CharacterString>1.2</gco:CharacterString>
            </gmd:metadataStandardVersion>
            <xsl:apply-templates select="resource_id"/>
            <gmd:identificationInfo>
                <gmd:MD_DataIdentification>
                    <gmd:citation>
                        <gmd:CI_Citation>
                            <gmd:title>
                                <gco:CharacterString>
                                    <xsl:value-of select="title"/>
                                </gco:CharacterString>
                            </gmd:title>
                            <gmd:date>
                                <gmd:CI_Date>
                                    <xsl:choose>
                                        <xsl:when test="publication_date">
                                            <gmd:date>
                                                <gco:DateTime>
                                                    <xsl:value-of select="publication_date"/>
                                                </gco:DateTime>
                                            </gmd:date>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <gmd:date gco:nilReason="missing">
                                                <gco:DateTime>
                                                    1900-01-01T00:00:00
                                                </gco:DateTime>
                                            </gmd:date>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                    <gmd:dateType>
                                        <gmd:CI_DateTypeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="publication">publication</gmd:CI_DateTypeCode>
                                    </gmd:dateType>
                                </gmd:CI_Date>
                            </gmd:date>
                            <gmd:citedResponsibleParty>
                                <gmd:CI_ResponsibleParty>
                                    <xsl:apply-templates select="originator_contact_person_name"/>
                                    <xsl:apply-templates select="originator_contact_org_name"/>
                                    <xsl:apply-templates select="originator_contact_position_name"/>
                                    <gmd:contactInfo>
                                        <gmd:CI_Contact>
                                            <xsl:apply-templates select="originator_contact_phone_fax_flag"/>
                                            <xsl:apply-templates select="originator_contact_address_flag"/>
                                            <xsl:apply-templates select="originator_contact_url"/>
                                        </gmd:CI_Contact>
                                    </gmd:contactInfo>
                                    <gmd:role>
                                        <gmd:CI_RoleCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode" codeListValue="distributor">pointOfContact</gmd:CI_RoleCode>
                                    </gmd:role>
                                </gmd:CI_ResponsibleParty>
                            </gmd:citedResponsibleParty>
                            <xsl:apply-templates select="bibliographic_citation"/>
                        </gmd:CI_Citation>
                    </gmd:citation>
                    <gmd:abstract>
                        <gco:CharacterString>
                            <xsl:value-of select="description"/>
                        </gco:CharacterString>
                    </gmd:abstract>
                    <gmd:status>
                        <gmd:MD_ProgressCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_ProgressCode" codeListValue="completed">completed</gmd:MD_ProgressCode>
                    </gmd:status>
                    <xsl:apply-templates select="keywords_thematic_flag"/>
                    <xsl:apply-templates select="keywords_temporal_flag"/>
                    <xsl:apply-templates select="keywords_spatial_flag"/>
                    <xsl:apply-templates select="related_resource"/>
                    <xsl:apply-templates select="resource_languages"/>
                    <gmd:extent>
                        <gmd:EX_Extent>
                            <gmd:geographicElement>
                                <gmd:EX_GeographicBoundingBox>
                                    <gmd:extentTypeCode>
                                        <gco:Boolean>1</gco:Boolean>
                                    </gmd:extentTypeCode>
                                    <gmd:westBoundLongitude>
                                        <gco:Decimal>
                                            <xsl:value-of select="west_bounding_longitude"/>
                                        </gco:Decimal>
                                    </gmd:westBoundLongitude>
                                    <xsl:apply-templates select="east_bounding_longitude"/>
                                    <xsl:apply-templates select="south_bounding_latitude"/>
                                    <gmd:northBoundLatitude>
                                        <gco:Decimal>
                                            <xsl:value-of select="north_bounding_latitude"/>
                                        </gco:Decimal>
                                    </gmd:northBoundLatitude>
                                </gmd:EX_GeographicBoundingBox>
                            </gmd:geographicElement>
                        </gmd:EX_Extent>
                    </gmd:extent>
                    <xsl:apply-templates select="temporal_start_date"/>
                    <xsl:apply-templates select="extent_flag"/>
                </gmd:MD_DataIdentification>
            </gmd:identificationInfo>
            <xsl:apply-templates select="resource_flag"/>
            <xsl:apply-templates select="data_quality_flag"/>
            <xsl:apply-templates select="resource_constraints_statement"/>
        </gmd:MD_Metadata>
    </xsl:template>

    <xsl:template match="metadata_uuid">
        <gmd:fileIdentifier>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:fileIdentifier>
    </xsl:template>

    <xsl:template match="resource_type">
        <gmd:hierarchyLevel>
            <gmd:MD_ScopeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_ScopeCode" codeListValue="">
                <xsl:attribute name="codeListValue">
                    <xsl:value-of select="//hierarchy_level"></xsl:value-of>
                </xsl:attribute>
                <xsl:value-of select="//hierarchy_level"></xsl:value-of>
            </gmd:MD_ScopeCode>
        </gmd:hierarchyLevel>
        <gmd:hierarchyLevelName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:hierarchyLevelName>
    </xsl:template>

    <xsl:template match="metadata_contact_person_name">
        <gmd:individualName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:individualName>
    </xsl:template>

    <xsl:template match="metadata_contact_name">
        <gmd:organisationName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:organisationName>
    </xsl:template>

    <xsl:template match="metadata_contact_org_name">
        <gmd:organisationName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:organisationName>
    </xsl:template>

    <xsl:template match="metadata_contact_position_name">
        <gmd:positionName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:positionName>
    </xsl:template>

    <xsl:template match="metadata_phone_fax_flag">
        <gmd:phone>
            <gmd:CI_Telephone>
                <xsl:apply-templates select="//metadata_contact_phone"/>
                <xsl:apply-templates select="//metadata_contact_fax"/>
            </gmd:CI_Telephone>
        </gmd:phone>
    </xsl:template>

    <xsl:template match="metadata_contact_phone">
        <gmd:voice>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:voice>
    </xsl:template>

    <xsl:template match="metadata_contact_fax">
        <gmd:facsimile>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:facsimile>
    </xsl:template>

    <xsl:template match="metadata_contact_street_address">
        <gmd:deliveryPoint>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:deliveryPoint>
    </xsl:template>

    <xsl:template match="metadata_contact_city">
        <gmd:city>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:city>
    </xsl:template>

    <xsl:template match="metadata_contact_state">
        <gmd:administrativeArea>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:administrativeArea>
    </xsl:template>

    <xsl:template match="metadata_contact_zip">
        <gmd:postalCode>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:postalCode>
    </xsl:template>

    <xsl:template match="metadata_contact_url">
        <gmd:onlineResource>
            <gmd:CI_OnlineResource>
                <gmd:linkage>
                    <gmd:URL>
                        <xsl:value-of select="."/>
                    </gmd:URL>
                </gmd:linkage>
            </gmd:CI_OnlineResource>
        </gmd:onlineResource>
    </xsl:template>

    <xsl:template match="resource_id">
        <gmd:dataSetURI>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:dataSetURI>
    </xsl:template>

    <xsl:template match="originator_contact_person_name">
        <gmd:individualName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:individualName>
    </xsl:template>

    <xsl:template match="originator_contact_org_name">
        <gmd:organisationName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:organisationName>
    </xsl:template>

    <xsl:template match="originator_contact_position_name">
        <gmd:positionName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:positionName>
    </xsl:template>

    <xsl:template match="originator_contact_phone_fax_flag">
        <gmd:phone>
            <gmd:CI_Telephone>
                <xsl:apply-templates select="//originator_contact_phone"/>
                <xsl:apply-templates select="//originator_contact_fax"/>
            </gmd:CI_Telephone>
        </gmd:phone>
    </xsl:template>

    <xsl:template match="//originator_contact_phone">
        <gmd:voice>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:voice>
    </xsl:template>

    <xsl:template match="//originator_contact_fax">
        <gmd:facsimile>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:facsimile>
    </xsl:template>

    <xsl:template match="originator_contact_address_flag">
        <gmd:address>
            <gmd:CI_Address>
                <xsl:apply-templates select="//originator_contact_street_address"/>
                <xsl:apply-templates select="//originator_contact_city"/>
                <xsl:apply-templates select="//originator_contact_state"/>
                <xsl:apply-templates select="//originator_contact_zip"/>
                <xsl:apply-templates select="//originator_contact_email"/>
            </gmd:CI_Address>
        </gmd:address>
    </xsl:template>

    <xsl:template match="//originator_contact_street_address">
        <gmd:deliveryPoint>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:deliveryPoint>
    </xsl:template>

    <xsl:template match="//originator_contact_city">
        <gmd:city>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:city>
    </xsl:template>

    <xsl:template match="//originator_contact_state">
        <gmd:administrativeArea>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:administrativeArea>
    </xsl:template>

    <xsl:template match="//originator_contact_zip">
        <gmd:postalCode>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:postalCode>
    </xsl:template>

    <xsl:template match="//originator_contact_email">
        <gmd:electronicMailAddress>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:electronicMailAddress>
    </xsl:template>

    <xsl:template match="originator_contact_url">
        <gmd:onlineResource>
            <gmd:CI_OnlineResource>
                <gmd:linkage>
                    <gmd:URL>
                        <xsl:value-of select="."/>
                    </gmd:URL>
                </gmd:linkage>
            </gmd:CI_OnlineResource>
        </gmd:onlineResource>
    </xsl:template>

    <xsl:template match="bibliographic_citation">
        <gmd:otherCitationDetails>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:otherCitationDetails>
    </xsl:template>

    <xsl:template match="keywords_thematic_flag">
        <gmd:descriptiveKeywords>
            <gmd:MD_Keywords>
                <xsl:apply-templates select="//keywords_thematic"/>
                <gmd:type>
                    <gmd:MD_KeywordTypeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_KeywordTypeCode" codeListValue="theme">theme</gmd:MD_KeywordTypeCode>
                </gmd:type>
            </gmd:MD_Keywords>
        </gmd:descriptiveKeywords>
    </xsl:template>

    <xsl:template match="//keywords_thematic">
        <gmd:keyword>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:keyword>
    </xsl:template>

    <xsl:template match="keywords_temporal_flag">
        <gmd:descriptiveKeywords>
            <gmd:MD_Keywords>
                <xsl:apply-templates select="//keywords_temporal"/>
                <gmd:type>
                    <gmd:MD_KeywordTypeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_KeywordTypeCode" codeListValue="temporal">temporal</gmd:MD_KeywordTypeCode>
                </gmd:type>
            </gmd:MD_Keywords>
        </gmd:descriptiveKeywords>
    </xsl:template>

    <xsl:template match="//keywords_temporal">
        <gmd:keyword>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:keyword>
    </xsl:template>

    <xsl:template match="keywords_spatial_flag">
        <gmd:descriptiveKeywords>
            <gmd:MD_Keywords>
                <xsl:apply-templates select="//keywords_spatial"/>
                <gmd:type>
                    <gmd:MD_KeywordTypeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_KeywordTypeCode" codeListValue="place">place</gmd:MD_KeywordTypeCode>
                </gmd:type>
            </gmd:MD_Keywords>
        </gmd:descriptiveKeywords>
    </xsl:template>

    <xsl:template match="//keywords_spatial">
        <gmd:keyword>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:keyword>
    </xsl:template>

    <xsl:template match="related_resource">
        <gmd:aggregationInfo>
            <!-- (?-C) MD_AggregateInformation requires either aggregateDataSetName/CI_Citation or aggregateDataSetIdentifier/MD_Identifier.   -->
            <gmd:MD_AggregateInformation>
                <gmd:aggregateDataSetIdentifier>
                    <gmd:MD_Identifier>
                        <gmd:code>
                            <gco:CharacterString>
                                <xsl:value-of select="identifier_code"/>
                            </gco:CharacterString>
                        </gmd:code>
                    </gmd:MD_Identifier>
                </gmd:aggregateDataSetIdentifier>
                <!-- (M-M) Association Type is mandatory.. -->
                <gmd:associationType>
                    <gmd:DS_AssociationTypeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#DS_AssociationTypeCode" codeListValue="crossReference">
                        <xsl:value-of select="association_type_code"/>
                    </gmd:DS_AssociationTypeCode>
                </gmd:associationType>
            </gmd:MD_AggregateInformation>
        </gmd:aggregationInfo>
    </xsl:template>

    <xsl:template match="resource_languages">
        <gmd:language>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:language>
    </xsl:template>

    <xsl:template match="east_bounding_longitude">
        <gmd:eastBoundLongitude>
            <gco:Decimal>
                <xsl:value-of select="."/>
            </gco:Decimal>
        </gmd:eastBoundLongitude>
    </xsl:template>

    <xsl:template match="south_bounding_latitude">
        <gmd:southBoundLatitude>
            <gco:Decimal>
                <xsl:value-of select="."/>
            </gco:Decimal>
        </gmd:southBoundLatitude>
    </xsl:template>

    <xsl:template match="temporal_start_date">
        <gmd:extent>
            <gmd:EX_Extent>
                <gmd:temporalElement>
                    <gmd:EX_TemporalExtent>
                        <gmd:extent>
                            <gml:TimePeriod>
                                <gml:name></gml:name>
                                <gml:beginPosition frame="#ISO-8601">
                                    <xsl:value-of select="."/>
                                </gml:beginPosition>
                                <gml:endPosition frame="#ISO-8601">
                                    <xsl:value-of select="//temporal_end_date"/>
                                </gml:endPosition>
                            </gml:TimePeriod>
                        </gmd:extent>
                    </gmd:EX_TemporalExtent>
                </gmd:temporalElement>
            </gmd:EX_Extent>
        </gmd:extent>
    </xsl:template>

    <xsl:template match="extent_flag">
        <gmd:extent>
            <gmd:EX_Extent>
                <gmd:verticalElement>
                    <gmd:EX_VerticalExtent>
                        <xsl:apply-templates select="//interval_depth_bottom"/>
                        <xsl:apply-templates select="//interval_depth_top"/>
                        <xsl:apply-templates select="//surface_elevation"/>
                    </gmd:EX_VerticalExtent>
                </gmd:verticalElement>
            </gmd:EX_Extent>
        </gmd:extent>
    </xsl:template>

    <xsl:template match="//interval_depth_bottom">
        <gmd:minimumValue>
            <gco:Real>
                <xsl:value-of select="."/>
            </gco:Real>
        </gmd:minimumValue>
    </xsl:template>

    <xsl:template match="//interval_depth_top">
        <gmd:maximumValue>
            <gco:Real>
                <xsl:value-of select="."/>
            </gco:Real>
        </gmd:maximumValue>
    </xsl:template>

    <xsl:template match="//surface_elevation">
        <gmd:verticalCRS xlink:href="">
            <xsl:attribute name="xlink:href">
                <xsl:value-of select="."></xsl:value-of>
            </xsl:attribute>
        </gmd:verticalCRS>
    </xsl:template>

    <xsl:template match="resource_flag">
        <gmd:distributionInfo>
            <gmd:MD_Distribution>
                <xsl:apply-templates select="//resource_distributor_flag"/>
                <xsl:apply-templates select="//resource_url"/>
            </gmd:MD_Distribution>
        </gmd:distributionInfo>
    </xsl:template>

    <xsl:template match="//resource_distributor_flag">
        <gmd:distributor>
            <gmd:MD_Distributor>
                <xsl:apply-templates select="//resource_distributor_responsibleparty_flag"/>
                <xsl:apply-templates select="//resource_access_instruction"/>
            </gmd:MD_Distributor>
        </gmd:distributor>
    </xsl:template>

    <xsl:template match="//resource_distributor_responsibleparty_flag">
        <gmd:distributorContact>
            <gmd:CI_ResponsibleParty>
                <xsl:apply-templates select="//distributor_contact_person_name"/>
                <xsl:apply-templates select="//distributor_contact_org_name"/>
                <xsl:apply-templates select="//distributor_contact_position_name"/>
                <xsl:apply-templates select="//resource_distributor_responsibleparty_contact_flag"/>
                <gmd:role>
                    <gmd:CI_RoleCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode" codeListValue="distributor">distributor</gmd:CI_RoleCode>
                </gmd:role>
            </gmd:CI_ResponsibleParty>
        </gmd:distributorContact>
    </xsl:template>

    <xsl:template match="//distributor_contact_person_name">
        <gmd:individualName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:individualName>
    </xsl:template>

    <xsl:template match="//distributor_contact_org_name">
        <gmd:organisationName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:organisationName>
    </xsl:template>

    <xsl:template match="//distributor_contact_position_name">
        <gmd:positionName>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:positionName>
    </xsl:template>

    <xsl:template match="//resource_distributor_responsibleparty_contact_flag">
        <gmd:contactInfo>
            <gmd:CI_Contact>
                <xsl:apply-templates
                        select="//resource_distributor_responsibleparty_contact_phone_fax_flag"/>
                <xsl:apply-templates
                        select="//resource_distributor_responsibleparty_contact_address_flag"/>
                <xsl:apply-templates select="//distributor_contact_url"/>
            </gmd:CI_Contact>
        </gmd:contactInfo>
    </xsl:template>

    <xsl:template
            match="//resource_distributor_responsibleparty_contact_phone_fax_flag">
        <gmd:phone>
            <gmd:CI_Telephone>
                <xsl:apply-templates select="//distributor_contact_phone"/>
                <xsl:apply-templates select="//distributor_contact_fax"/>
            </gmd:CI_Telephone>
        </gmd:phone>
    </xsl:template>

    <xsl:template match="//distributor_contact_phone">
        <gmd:voice>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:voice>
    </xsl:template>

    <xsl:template match="//distributor_contact_fax">
        <gmd:facsimile>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:facsimile>
    </xsl:template>

    <xsl:template
            match="//resource_distributor_responsibleparty_contact_address_flag">
        <gmd:address>
            <gmd:CI_Address>
                <xsl:apply-templates select="//distributor_contact_street_address"/>
                <xsl:apply-templates select="//distributor_contact_city"/>
                <xsl:apply-templates select="//distributor_contact_state"/>
                <xsl:apply-templates select="//distributor_contact_zip"/>
                <gmd:country>
                    <gco:CharacterString>USA</gco:CharacterString>
                </gmd:country>
                <xsl:apply-templates select="//distributor_contact_email"/>
            </gmd:CI_Address>
        </gmd:address>
    </xsl:template>

    <xsl:template match="//distributor_contact_street_address">
        <gmd:deliveryPoint>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:deliveryPoint>
    </xsl:template>

    <xsl:template match="//distributor_contact_city">
        <gmd:city>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:city>
    </xsl:template>

    <xsl:template match="//distributor_contact_state">
        <gmd:administrativeArea>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:administrativeArea>
    </xsl:template>

    <xsl:template match="//distributor_contact_zip">
        <gmd:postalCode>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:postalCode>
    </xsl:template>

    <xsl:template match="//distributor_contact_email">
        <gmd:electronicMailAddress>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:electronicMailAddress>
    </xsl:template>

    <xsl:template match="//distributor_contact_url">
        <gmd:onlineResource>
            <gmd:CI_OnlineResource>
                <gmd:linkage>
                    <gmd:URL>
                        <xsl:value-of select="."/>
                    </gmd:URL>
                </gmd:linkage>
            </gmd:CI_OnlineResource>
        </gmd:onlineResource>
    </xsl:template>

    <xsl:template match="//resource_access_instruction">
        <gmd:distributionOrderProcess>
            <gmd:MD_StandardOrderProcess>
                <gmd:orderingInstructions>
                    <gco:CharacterString>
                        <xsl:value-of select="."/>
                    </gco:CharacterString>
                </gmd:orderingInstructions>
            </gmd:MD_StandardOrderProcess>
        </gmd:distributionOrderProcess>
    </xsl:template>

    <xsl:template match="//resource_url">
        <gmd:transferOptions>
            <gmd:MD_DigitalTransferOptions>
                <gmd:onLine>
                    <gmd:CI_OnlineResource>
                        <gmd:linkage>
                            <gmd:URL>
                                <xsl:value-of select="url"/>
                            </gmd:URL>
                        </gmd:linkage>
                        <xsl:apply-templates select="name"/>
                    </gmd:CI_OnlineResource>
                </gmd:onLine>
            </gmd:MD_DigitalTransferOptions>
        </gmd:transferOptions>
    </xsl:template>

    <xsl:template match="name">
        <gmd:name>
            <gco:CharacterString>
                <xsl:value-of select="."/>
            </gco:CharacterString>
        </gmd:name>
    </xsl:template>

    <xsl:template match="data_quality_flag">
        <gmd:dataQualityInfo>
            <gmd:DQ_DataQuality>
                <gmd:scope>
                    <gmd:DQ_Scope>
                        <gmd:level>
                            <gmd:MD_ScopeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_ScopeCode" codeListValue="dataset">dataset</gmd:MD_ScopeCode>
                        </gmd:level>
                    </gmd:DQ_Scope>
                </gmd:scope>
                <xsl:apply-templates select="//resource_quality_statement"/>
                <xsl:apply-templates select="//resource_lineage_statement"/>
            </gmd:DQ_DataQuality>
        </gmd:dataQualityInfo>
    </xsl:template>

    <xsl:template match="//resource_quality_statement">
        <gmd:report>
            <gmd:DQ_QuantitativeAttributeAccuracy> <!-- this element is ignored, its just a container for the result explanation -->
                <gmd:result>
                    <gmd:DQ_ConformanceResult>
                        <gmd:specification gco:nilReason="inapplicable"/>
                        <gmd:explanation>
                            <gco:CharacterString>
                                <xsl:value-of select="."/>
                            </gco:CharacterString>
                        </gmd:explanation>
                        <gmd:pass gco:nilReason="inapplicable"/>
                    </gmd:DQ_ConformanceResult>
                </gmd:result>
            </gmd:DQ_QuantitativeAttributeAccuracy>
        </gmd:report>
    </xsl:template>

    <xsl:template match="//resource_lineage_statement">
        <gmd:lineage>
            <gmd:LI_Lineage>
                <gmd:statement>
                    <gco:CharacterString>
                        <xsl:value-of select="."/>
                    </gco:CharacterString>
                </gmd:statement>
            </gmd:LI_Lineage>
        </gmd:lineage>
    </xsl:template>

    <xsl:template match="resource_constraints_statement">
        <gmd:metadataConstraints>
            <gmd:MD_Constraints>
                <gmd:useLimitation>
                    <gco:CharacterString>
                        <xsl:value-of select="."/>
                    </gco:CharacterString>
                </gmd:useLimitation>
            </gmd:MD_Constraints>
        </gmd:metadataConstraints>
    </xsl:template>

</xsl:stylesheet>
	