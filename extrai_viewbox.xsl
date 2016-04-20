<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:svg="http://www.w3.org/2000/svg">

<xsl:output method="text"/>
<xsl:template match="text()">
</xsl:template>

<xsl:template match="svg:svg">
    <xsl:if test="@viewBox">
      <xsl:text>[</xsl:text>
      <xsl:value-of select="@viewBox"/>
      <xsl:text>]</xsl:text>
    </xsl:if>
    <xsl:if test="not(@viewBox)">
      <xsl:text>[0 0 </xsl:text>
      <xsl:value-of select="@width"/>
      <xsl:text> </xsl:text>
      <xsl:value-of select="@height"/>
      <xsl:text>]</xsl:text>
    </xsl:if>
</xsl:template>

</xsl:stylesheet>
