# $NetBSD$

DISTNAME=	naturalearth-10m
PKGNAME=	${DISTNAME}-5.1.1
CATEGORIES=	geography
MASTER_SITES=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/
COMMENT=	NaturalEarth 1:10m map
LICENSE=	cc0-1.0-universal

DISTFILES+=	10m_cultural.zip
SITES.10m_cultural.zip=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/

DISTFILES+=	10m_physical.zip
SITES.10m_physical.zip=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/

DISTFILES+=	HYP_HR_SR_OB_DR.zip
SITES.HYP_HR_SR_OB_DR.zip=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/

DISTFILES+=	NE1_HR_LC_SR_W_DR.zip
SITES.NE1_HR_LC_SR_W_DR.zip=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/

DISTFILES+=	NE2_HR_LC_SR_W_DR.zip
SITES.NE2_HR_LC_SR_W_DR.zip=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/

FETCH_USING=	custom
FETCH_CMD=	wget
FETCH_BEFORE_ARGS=	--referer https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/

USE_TOOLS+=	unzip
NO_BUILD=	yes
EXTRACT_ONLY=	
WRKSRC=	${WRKDIR}/${DISTNAME}

TOOLS_DEPENDS+=	unzip-[0-9]*:../../archivers/unzip
TOOLS_DEPENDS+=	wget-[0-9]*:../../net/wget

pre-extract:
	${MKDIR} ${WRKSRC}
	${MKDIR} ${WRKSRC}/10m_physical
	${MKDIR} ${WRKSRC}/10m_raster

do-extract:
	${UNZIP_CMD} -d ${WRKSRC} ${DISTDIR}/10m_cultural.zip
	${UNZIP_CMD} -d ${WRKSRC}/10m_physical ${DISTDIR}/10m_physical.zip
	${UNZIP_CMD} -d ${WRKSRC}/10m_raster ${DISTDIR}/HYP_HR_SR_OB_DR.zip
	${UNZIP_CMD} -d ${WRKSRC}/10m_raster ${DISTDIR}/NE1_HR_LC_SR_W_DR.zip
	${UNZIP_CMD} -d ${WRKSRC}/10m_raster ${DISTDIR}/NE2_HR_LC_SR_W_DR.zip

pre-install:
	${MKDIR} ${DESTDIR}${PREFIX}/share/${DISTNAME}
	${MKDIR} ${DESTDIR}${PREFIX}/share/${DISTNAME}/10m_cultural
	${MKDIR} ${DESTDIR}${PREFIX}/share/${DISTNAME}/10m_physical
	${MKDIR} ${DESTDIR}${PREFIX}/share/${DISTNAME}/10m_raster

do-install:
.for datafile in ${WRKSRC}/CHANGELOG ${WRKSRC}/README.md ${WRKSRC}/VERSION
	${INSTALL_DATA} ${WRKDIR}/${datafile} ${DESTDIR}${PREFIX}/share/${DISTNAME}
.endfor
.for datadir in ${WRKSRC}/10m_cultural ${WRKSRC}/10m_physical ${WRKSRC}/10m_raster
	${CP} -pr ${WRKDIR}/${datadir} ${DESTDIR}${PREFIX}/share/${DISTNAME}
.endfor

# url2pkg-marker (please do not remove this line.)
.include "../../mk/bsd.pkg.mk"
