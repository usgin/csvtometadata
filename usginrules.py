from xmlvalidator import ExistsRule, ValueInListRule, ConditionalRule, ContentMatchesExpressionRule, AnyOfRule

class UsginMinRules(list):
    def __init__(self):
        list.__init__(self)

        condition = ExistsRule(name='IdentificationInfo: Record is a Dataset',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification')
        requirement = ValueInListRule(name='Dataset: Resource Language Code for Dataset is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:language/gco:CharacterString',values=['aar', 'abk', 'ace', 'ach', 'ada', 'ady', 'afa', 'afh', 'afr', 'ain', 'aka', 'akk', 'ale', 'alg', 'alt', 'amh', 'ang', 'anp', 'apa', 'ara', 'arc', 'arg', 'arn', 'arp', 'art', 'arw', 'asm', 'ast', 'ath', 'aus', 'ava', 'ave', 'awa', 'aym', 'aze', 'bad', 'bai', 'bak', 'bal', 'bam', 'ban', 'bas', 'bat', 'bej', 'bel', 'bem', 'ben', 'ber', 'bho', 'bih', 'bik', 'bin', 'bis', 'bla', 'bnt', 'bos', 'bra', 'bre', 'btk', 'bua', 'bug', 'bul', 'byn', 'cad', 'cai', 'car', 'cat', 'cau', 'ceb', 'cel', 'cha', 'chb', 'che', 'chg', 'chk', 'chm', 'chn', 'cho', 'chp', 'chr', 'chu', 'chv', 'chy', 'cmc', 'cop', 'cor', 'cos', 'cpe', 'cpf', 'cpp', 'cre', 'crh', 'crp', 'csb', 'cus', 'dak', 'dan', 'dar', 'day', 'del', 'den', 'dgr', 'din', 'div', 'doi', 'dra', 'dsb', 'dua', 'dum', 'dyu', 'dzo', 'efi', 'egy', 'eka', 'elx', 'eng', 'enm', 'epo', 'est', 'ewe', 'ewo', 'fan', 'fao', 'fat', 'fij', 'fil', 'fin', 'fiu', 'fon', 'frm', 'fro', 'frr', 'frs', 'fry', 'ful', 'fur', 'gaa', 'gay', 'gba', 'gem', 'gez', 'gil', 'gla', 'gle', 'glg', 'glv', 'gmh', 'goh', 'gon', 'gor', 'got', 'grb', 'grc', 'grn', 'gsw', 'guj', 'gwi', 'hai', 'hat', 'hau', 'haw', 'heb', 'her', 'hil', 'him', 'hin', 'hit', 'hmn', 'hmo', 'hrv', 'hsb', 'hun', 'hup', 'iba', 'ibo', 'ido', 'iii', 'ijo', 'iku', 'ile', 'ilo', 'ina', 'inc', 'ind', 'ine', 'inh', 'ipk', 'ira', 'iro', 'ita', 'jav', 'jbo', 'jpn', 'jpr', 'jrb', 'kaa', 'kab', 'kac', 'kal', 'kam', 'kan', 'kar', 'kas', 'kau', 'kaw', 'kaz', 'kbd', 'kha', 'khi', 'khm', 'kho', 'kik', 'kin', 'kir', 'kmb', 'kok', 'kom', 'kon', 'kor', 'kos', 'kpe', 'krc', 'krl', 'kro', 'kru', 'kua', 'kum', 'kur', 'kut', 'lad', 'lah', 'lam', 'lao', 'lat', 'lav', 'lez', 'lim', 'lin', 'lit', 'lol', 'loz', 'ltz', 'lua', 'lub', 'lug', 'lui', 'lun', 'luo', 'lus', 'mad', 'mag', 'mah', 'mai', 'mak', 'mal', 'man', 'map', 'mar', 'mas', 'mdf', 'mdr', 'men', 'mga', 'mic', 'min', 'mis', 'mkh', 'mlg', 'mlt', 'mnc', 'mni', 'mno', 'moh', 'mon', 'mos', 'mul', 'mun', 'mus', 'mwl', 'mwr', 'myn', 'myv', 'nah', 'nai', 'nap', 'nau', 'nav', 'nbl', 'nde', 'ndo', 'nds', 'nep', 'new', 'nia', 'nic', 'niu', 'nno', 'nob', 'nog', 'non', 'nor', 'nqo', 'nso', 'nub', 'nwc', 'nya', 'nym', 'nyn', 'nyo', 'nzi', 'oci', 'oji', 'ori', 'orm', 'osa', 'oss', 'ota', 'oto', 'paa', 'pag', 'pal', 'pam', 'pan', 'pap', 'pau', 'peo', 'phi', 'phn', 'pli', 'pol', 'pon', 'por', 'pra', 'pro', 'pus', 'que', 'raj', 'rap', 'rar', 'roa', 'roh', 'rom', 'run', 'rup', 'rus', 'sad', 'sag', 'sah', 'sai', 'sal', 'sam', 'san', 'sas', 'sat', 'scn', 'sco', 'sel', 'sem', 'sga', 'sgn', 'shn', 'sid', 'sin', 'sio', 'sit', 'sla', 'slv', 'sma', 'sme', 'smi', 'smj', 'smn', 'smo', 'sms', 'sna', 'snd', 'snk', 'sog', 'som', 'son', 'sot', 'spa', 'srd', 'srn', 'srp', 'srr', 'ssa', 'ssw', 'suk', 'sun', 'sus', 'sux', 'swa', 'swe', 'syc', 'syr', 'tah', 'tai', 'tam', 'tat', 'tel', 'tem', 'ter', 'tet', 'tgk', 'tgl', 'tha', 'tig', 'tir', 'tiv', 'tkl', 'tlh', 'tli', 'tmh', 'tog', 'ton', 'tpi', 'tsi', 'tsn', 'tso', 'tuk', 'tum', 'tup', 'tur', 'tut', 'tvl', 'twi', 'tyv', 'udm', 'uga', 'uig', 'ukr', 'umb', 'und', 'urd', 'uzb', 'vai', 'ven', 'vie', 'vol', 'vot', 'wak', 'wal', 'war', 'was', 'wen', 'wln', 'wol', 'xal', 'xho', 'yao', 'yap', 'yid', 'yor', 'ypk', 'zap', 'zbl', 'zen', 'zha', 'znd', 'zul', 'zun', 'zxx', 'zza'])
        rule = ConditionalRule(name='Dataset: Resource Language Code is Valid',description='not given',rule_set=[condition, requirement])
        self.append(rule)
        
        condition = ExistsRule(name='DistributionInfo: is Present',description='not given',xpath='//gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution')
        requirement = ExistsRule(name='DistributionInfo: Transfer Options are Included',description='not given',xpath='//gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions')
        rule = ConditionalRule(name='DistributionInfo: Requires Transfer Options',description='not given',rule_set=[condition, requirement])
        self.append(rule)
        
        condition = ExistsRule(name='DistributionInfo: is Present',description='not given',xpath='//gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution')
        requirement = ValueInListRule(name='DistributionInfo: Distributor RoleCode codeList is valid',description='not given',xpath='//gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode/@codeList',values=['http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode'])
        rule = ConditionalRule(name='DistributionInfo: Requires that Distributor RoleCode codeList is Valid',description='not given',rule_set=[condition, requirement])
        self.append(rule)
        
        condition = ExistsRule(name='DistributionInfo: is Present',description='not given',xpath='//gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution')
        requirement = ValueInListRule(name='DistributionInfo: Distributor RoleCode codeListValue is valid',description='not given',xpath='//gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode/@codeListValue',values=['author', 'custodian', 'distributor', 'originator', 'owner', 'pointOfContact', 'principalInvestigator', 'processor', 'publisher', 'resourceProvider', 'user'])
        rule = ConditionalRule(name='DistributionInfo: Requires that Distributor RoleCode codeListValue is valid',description='not given',rule_set=[condition, requirement])
        self.append(rule)
        
        condition = ExistsRule(name='DistributionInfo: is Present',description='not given',xpath='//gmd:MD_Metadata/gmd:distributionInfo/gmd:MD_Distribution')
        requirement = AnyOfRule(name='DistributionInfo: Distributor has a named Entity',description='not given',xpaths=[u'/gmd:individualName', u'/gmd:organisationName', u'/gmd:positionName'],context='//gmd:distributor/gmd:MD_Distributor/gmd:distributorContact/gmd:CI_ResponsibleParty')
        rule = ConditionalRule(name='DistributionInfo: requires Distributor with Named Entity',description='not given',rule_set=[condition, requirement])
        self.append(rule)
        
        rule = ExistsRule(name='IdentificationInfo: A CI_Citation is Required',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation')
        self.append(rule)
        
        rule = ExistsRule(name='IdentificationInfo: Abstract exists',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:abstract/gco:CharacterString')
        self.append(rule)
        
        rule = ContentMatchesExpressionRule(name='IdentificationInfo: CI_Citation DateTime is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime',expression='^[1-2][0-9]{3}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-6][0-9]:[0-6][0-9]$')
        self.append(rule)
        
        rule = ValueInListRule(name='IdentificationInfo: CI_Citation DateTypeCode codeList is valid',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode/@codeList',values=['http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode'])
        self.append(rule)
        
        rule = ValueInListRule(name='IdentificationInfo: CI_Citation DateTypeCode codeListValue  is valid',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode/@codeListValue',values=['creation', 'publication', 'revision'])
        self.append(rule)
        
        rule = ExistsRule(name='IdentificationInfo: CI_Citation Requires a Title',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString')
        self.append(rule)
        
        rule = ValueInListRule(name='IdentificationInfo: CI_Citation RoleCode codeList is valid',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode/@codeList',values=['http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode'])
        self.append(rule)
        
        rule = ValueInListRule(name='IdentificationInfo: CI_Citation RoleCode codeListValue is valid',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode/@codeListValue',values=['author', 'custodian', 'distributor', 'originator', 'owner', 'pointOfContact', 'principalInvestigator', 'processor', 'publisher', 'resourceProvider', 'user'])
        self.append(rule)
        
        rule = ValueInListRule(name='IdentificationInfo: Status codeList for Resource is valid',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:status/gmd:MD_ProgressCode/@codeList',values=['http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_ProgressCode'])
        self.append(rule)
        
        rule = ValueInListRule(name='IdentificationInfo: Status codeListValue for Resource is valid',description='not given',xpath='//gmd:MD_Metadata/gmd:identificationInfo//gmd:status/gmd:MD_ProgressCode/@codeListValue',values=['completed', 'historicalArchive', 'obsolete', 'onGoing', 'planned', 'required', 'underDevelopment'])
        self.append(rule)
        
        rule = AnyOfRule(name='Intellectual Contact: Must have a named entity',description='not given',xpaths=[u'/gmd:individualName/gco:CharacterString', u'/gmd:organisationName/gco:CharacterString', u'/gmd:positionName/gco:CharacterString'],context='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty')
        self.append(rule)
        
        rule = AnyOfRule(name='Intellectual Contact: Must have a some Contact Info',description='not given',xpaths=[u'/gmd:phone/gmd:CI_Telephone/gmd:voice/gco:CharacterString', u'/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString', u'/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString'],context='//gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:citedResponsibleParty/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact')
        self.append(rule)
        
        rule = AnyOfRule(name='Metadata Contact: Must have a named entity',description='not given',xpaths=[u'/gmd:individualName/gco:CharacterString', u'/gmd:organisationName/gco:CharacterString', u'/gmd:positionName/gco:CharacterString'],context='//gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty')
        self.append(rule)
        
        rule = ContentMatchesExpressionRule(name='Metadata Contact: Must have an email address',description='not given',xpath='//gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString',expression='^.+@.+\..+$')
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata Contact: Role codeList is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode/@codeList',values=['http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#CI_RoleCode'])
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata Contact: Role codeListValue is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:role/gmd:CI_RoleCode/@codeListValue',values=['author', 'custodian', 'distributor', 'originator', 'owner', 'pointOfContact', 'principalInvestigator', 'processor', 'publisher', 'resourceProvider', 'user'])
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata: CharacterSetCode codeList is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:characterSet/gmd:MD_CharacterSetCode/@codeList',values=['http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_CharacterSetCode'])
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata: CharacterSetCode codeListValue is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:characterSet/gmd:MD_CharacterSetCode/@codeListValue',values=['8859part1', '8859part10', '8859part11', '8859part13', '8859part14', '8859part15', '8859part16', '8859part2', '8859part3', '8859part4', '8859part5', '8859part6', '8859part7', '8859part8', '8859part9', 'GB2312', 'big5', 'ebcdic', 'eucJP', 'eucKR', 'jis', 'shiftJIS', 'ucs2', 'ucs4', 'usAscii', 'utf16', 'utf7', 'utf8'])
        self.append(rule)
        
        rule = ContentMatchesExpressionRule(name='Metadata: DateStamp looks like an ISO date',description='not given',xpath='//gmd:MD_Metadata/gmd:dateStamp/gco:DateTime',expression='^[1-2][0-9]{3}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-6][0-9]:[0-6][0-9]$')
        self.append(rule)
        
        rule = ExistsRule(name='Metadata: Has File Identifier',description='not given',xpath='//gmd:MD_Metadata/gmd:fileIdentifier/gco:CharacterString')
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata: HierarchyLevel codeList is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:hierarchyLevel/gmd:MD_ScopeCode/@codeList',values=['http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/gmxCodelists.xml#MD_ScopeCode'])
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata: HierarchyLevel codeListValue is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:hierarchyLevel/gmd:MD_ScopeCode/@codeListValue',values=['attribute', 'attributeType', 'collectionHardware', 'collectionSession', 'dataset', 'dimensionGroup', 'feature', 'featureType', 'fieldSession', 'model', 'nonGeographicDataset', 'propertyType', 'series', 'service', 'software', 'tile'])
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata: HierarchyLevelName is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:hierarchyLevelName/gco:CharacterString',values=['Dataset', 'Service'])
        self.append(rule)
        
        condition = ValueInListRule(name='Metadata: Icon is labeled',description='not given',xpath='//gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:onlineResource/gmd:CI_OnlineResource/gmd:name/gco:CharacterString',values=['icon'])
        requirement = ContentMatchesExpressionRule(name='Metadata: URL is required',description='not given',xpath='//gmd:MD_Metadata/gmd:contact/gmd:CI_ResponsibleParty/gmd:contactInfo/gmd:CI_Contact/gmd:onlineResource/gmd:CI_OnlineResource/gmd:linkage/gmd:URL',expression='^http://.+\..+$')
        rule = ConditionalRule(name='Metadata: If Contact provides an Icon, a URL must be provided',description='not given',rule_set=[condition, requirement])
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata: Language Code is Valid',description='not given',xpath='//gmd:MD_Metadata/gmd:language/gco:CharacterString',values=['aar', 'abk', 'ace', 'ach', 'ada', 'ady', 'afa', 'afh', 'afr', 'ain', 'aka', 'akk', 'ale', 'alg', 'alt', 'amh', 'ang', 'anp', 'apa', 'ara', 'arc', 'arg', 'arn', 'arp', 'art', 'arw', 'asm', 'ast', 'ath', 'aus', 'ava', 'ave', 'awa', 'aym', 'aze', 'bad', 'bai', 'bak', 'bal', 'bam', 'ban', 'bas', 'bat', 'bej', 'bel', 'bem', 'ben', 'ber', 'bho', 'bih', 'bik', 'bin', 'bis', 'bla', 'bnt', 'bos', 'bra', 'bre', 'btk', 'bua', 'bug', 'bul', 'byn', 'cad', 'cai', 'car', 'cat', 'cau', 'ceb', 'cel', 'cha', 'chb', 'che', 'chg', 'chk', 'chm', 'chn', 'cho', 'chp', 'chr', 'chu', 'chv', 'chy', 'cmc', 'cop', 'cor', 'cos', 'cpe', 'cpf', 'cpp', 'cre', 'crh', 'crp', 'csb', 'cus', 'dak', 'dan', 'dar', 'day', 'del', 'den', 'dgr', 'din', 'div', 'doi', 'dra', 'dsb', 'dua', 'dum', 'dyu', 'dzo', 'efi', 'egy', 'eka', 'elx', 'eng', 'enm', 'epo', 'est', 'ewe', 'ewo', 'fan', 'fao', 'fat', 'fij', 'fil', 'fin', 'fiu', 'fon', 'frm', 'fro', 'frr', 'frs', 'fry', 'ful', 'fur', 'gaa', 'gay', 'gba', 'gem', 'gez', 'gil', 'gla', 'gle', 'glg', 'glv', 'gmh', 'goh', 'gon', 'gor', 'got', 'grb', 'grc', 'grn', 'gsw', 'guj', 'gwi', 'hai', 'hat', 'hau', 'haw', 'heb', 'her', 'hil', 'him', 'hin', 'hit', 'hmn', 'hmo', 'hrv', 'hsb', 'hun', 'hup', 'iba', 'ibo', 'ido', 'iii', 'ijo', 'iku', 'ile', 'ilo', 'ina', 'inc', 'ind', 'ine', 'inh', 'ipk', 'ira', 'iro', 'ita', 'jav', 'jbo', 'jpn', 'jpr', 'jrb', 'kaa', 'kab', 'kac', 'kal', 'kam', 'kan', 'kar', 'kas', 'kau', 'kaw', 'kaz', 'kbd', 'kha', 'khi', 'khm', 'kho', 'kik', 'kin', 'kir', 'kmb', 'kok', 'kom', 'kon', 'kor', 'kos', 'kpe', 'krc', 'krl', 'kro', 'kru', 'kua', 'kum', 'kur', 'kut', 'lad', 'lah', 'lam', 'lao', 'lat', 'lav', 'lez', 'lim', 'lin', 'lit', 'lol', 'loz', 'ltz', 'lua', 'lub', 'lug', 'lui', 'lun', 'luo', 'lus', 'mad', 'mag', 'mah', 'mai', 'mak', 'mal', 'man', 'map', 'mar', 'mas', 'mdf', 'mdr', 'men', 'mga', 'mic', 'min', 'mis', 'mkh', 'mlg', 'mlt', 'mnc', 'mni', 'mno', 'moh', 'mon', 'mos', 'mul', 'mun', 'mus', 'mwl', 'mwr', 'myn', 'myv', 'nah', 'nai', 'nap', 'nau', 'nav', 'nbl', 'nde', 'ndo', 'nds', 'nep', 'new', 'nia', 'nic', 'niu', 'nno', 'nob', 'nog', 'non', 'nor', 'nqo', 'nso', 'nub', 'nwc', 'nya', 'nym', 'nyn', 'nyo', 'nzi', 'oci', 'oji', 'ori', 'orm', 'osa', 'oss', 'ota', 'oto', 'paa', 'pag', 'pal', 'pam', 'pan', 'pap', 'pau', 'peo', 'phi', 'phn', 'pli', 'pol', 'pon', 'por', 'pra', 'pro', 'pus', 'que', 'raj', 'rap', 'rar', 'roa', 'roh', 'rom', 'run', 'rup', 'rus', 'sad', 'sag', 'sah', 'sai', 'sal', 'sam', 'san', 'sas', 'sat', 'scn', 'sco', 'sel', 'sem', 'sga', 'sgn', 'shn', 'sid', 'sin', 'sio', 'sit', 'sla', 'slv', 'sma', 'sme', 'smi', 'smj', 'smn', 'smo', 'sms', 'sna', 'snd', 'snk', 'sog', 'som', 'son', 'sot', 'spa', 'srd', 'srn', 'srp', 'srr', 'ssa', 'ssw', 'suk', 'sun', 'sus', 'sux', 'swa', 'swe', 'syc', 'syr', 'tah', 'tai', 'tam', 'tat', 'tel', 'tem', 'ter', 'tet', 'tgk', 'tgl', 'tha', 'tig', 'tir', 'tiv', 'tkl', 'tlh', 'tli', 'tmh', 'tog', 'ton', 'tpi', 'tsi', 'tsn', 'tso', 'tuk', 'tum', 'tup', 'tur', 'tut', 'tvl', 'twi', 'tyv', 'udm', 'uga', 'uig', 'ukr', 'umb', 'und', 'urd', 'uzb', 'vai', 'ven', 'vie', 'vol', 'vot', 'wak', 'wal', 'war', 'was', 'wen', 'wln', 'wol', 'xal', 'xho', 'yao', 'yap', 'yid', 'yor', 'ypk', 'zap', 'zbl', 'zen', 'zha', 'znd', 'zul', 'zun', 'zxx', 'zza'])
        self.append(rule)
        
        rule = AnyOfRule(name='Metadata: Resource Identification is Required',description='not given',xpaths=[u'/gmd:MD_DataIdentification', u'/srv:SV_ServiceIdentification'],context='//gmd:MD_Metadata/gmd:identificationInfo')
        self.append(rule)
        
        rule = ValueInListRule(name='Metadata: Standard Name is identified',description='not given',xpath='//gmd:MD_Metadata/gmd:metadataStandardName/gco:CharacterString',values=['ISO-NAP-USGIN'])
        self.append(rule)
        
        rule = ExistsRule(name='Metadata: Standard Version is identified',description='not given',xpath='//gmd:MD_Metadata/gmd:metadataStandardVersion/gco:CharacterString')
        self.append(rule)
