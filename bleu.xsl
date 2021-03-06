<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:svg="http://www.w3.org/2000/svg">

<xsl:output method="text" />
<xsl:template match="text()"></xsl:template>

<xsl:template match="svg:path">
    <!--<xsl:number level="any" />
    <xsl:text>:</xsl:text>
    <xsl:for-each select="(ancestor::*|.)[@transform]">
      <xsl:value-of select="@transform"/>
      <xsl:text> </xsl:text>
    </xsl:for-each>
    <xsl:text>:</xsl:text>
    <xsl:value-of select="@d"/>-->
    <xsl:value-of select="ancestor-or-self::*[@transform]/@transform" />
    <xsl:text>&#xa;</xsl:text>
</xsl:template>

</xsl:stylesheet>
