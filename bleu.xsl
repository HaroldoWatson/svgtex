<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:svg="http://www.w3.org/2000/svg"
xmlns:fn="http://www.w3.org/2005/xpath-functions"
>

<xsl:template match="text()">
</xsl:template>

<xsl:template name="bleu">
  <xsl:variable name="blum">
    1 2 3 4
  </xsl:variable>
  <xsl:for-each select="$blum">
    <xsl:value-of select="." />
  </xsl:for-each>
</xsl:template>

<xsl:template match="/">
    <xsl:value-of select="substring-before(substring-after('1999/04/01','/'),'/')"/>
</xsl:template>


</xsl:stylesheet>