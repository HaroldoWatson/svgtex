<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="path">
      <xsl:value-of select="@d"></xsl:value-of>  
    </xsl:template>
</xsl:stylesheet>