<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:svg="http://www.w3.org/2000/svg">

<xsl:output method="text" />
<!--<xsl:template match="text()">
</xsl:template>-->

<xsl:template match="svg:svg">
    <xsl:text>viewBox </xsl:text>
    <xsl:if test="@viewBox">
      <xsl:value-of select="@viewBox"/>
    </xsl:if>
    <xsl:if test="not(@viewBox)">
      <xsl:text>0 0 </xsl:text>
      <xsl:value-of select="@width"/>
      <xsl:text> </xsl:text>
      <xsl:value-of select="@height"/>
    </xsl:if>
    <xsl:apply-templates select="//svg:path"/>
</xsl:template>

<xsl:template match="svg:path">
    <xsl:text>id </xsl:text>
    <xsl:number level="any" />
    <xsl:text> </xsl:text>
    <xsl:for-each select="(ancestor::*|.)[@transform]">
      <xsl:value-of select="@transform"/>
      <xsl:text> </xsl:text>
    </xsl:for-each>
    <xsl:text> </xsl:text>
    <xsl:value-of select="@d"/>
    <xsl:text> </xsl:text>
</xsl:template>

</xsl:stylesheet>