# $NetBSD$

#CULTURAL=	10m_cultural.zip
#PHYSICAL=	10m_physical.zip
#RASTER1=	HYP_HR_SR_OB_DR.zip
#RASTER2=	NE1_HR_LC_SR_W_DR.zip
#RASTER3=	NE2_HR_LC_SR_W_DR.zip

DISTNAME=	# empty
PKGNAME=	naturalearth-10m-5.1.1
CATEGORIES=	geography
MASTER_SITES=	# empty
MASTER_SITE_BACKUP=	# empty
DISTFILES+=	10m_cultural.zip
SITES.10m_cultural.zip= https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/
DISTFILES+=	10m_physical.zip
SITES.10m_physical.zip= https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/
DISTFILES+=	HYP_HR_SR_OB_DR.zip
SITE.HYP_HR_SR_OB_DR.zip=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/
DISTFILES+=	NE1_HR_LC_SR_W_DR.zip
SITE.NE1_HR_LC_SR_W_DR.zip=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/
DISTFILES+=	NE2_HR_LC_SR_W_DR.zip
SITE.NE2_HR_LC_SR_W_DR.zip=	https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://www.naturalearthdata.com/
COMMENT=	NaturalEarth 1:10m map
LICENSE=	cc0-1.0-universal

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
	${MKDIR} ${WRKSRC}/naturalearth/10m_cultural
	${MKDIR} ${WRKSRC}/naturalearth/10m_physical
	${MKDIR} ${WRKSRC}/naturalearth/10m_raster

do-extract:
	${UNZIP_CMD} -d ${WRKSRC}/naturalearth ${DISTDIR}/10m_cultural.zip
	${MV} ${WRKSRC}/naturalearth/CHANGELOG ${WRKSRC}/naturalearth/10m_cultural/
	${MV} ${WRKSRC}/naturalearth/README.md ${WRKSRC}/naturalearth/10m_cultural/
	${MV} ${WRKSRC}/naturalearth/VERSION ${WRKSRC}/naturalearth/10m_cultural/
	${UNZIP_CMD} -d ${WRKSRC}/naturalearth/10m_physical ${DISTDIR}/10m_physical.zip
	${UNZIP_CMD} -d ${WRKSRC}/naturalearth/10m_raster ${DISTDIR}/HYP_HR_SR_OB_DR.zip
	${UNZIP_CMD} -d ${WRKSRC}/naturalearth/10m_raster ${DISTDIR}/NE1_HR_LC_SR_W_DR.zip
	${UNZIP_CMD} -d ${WRKSRC}/naturalearth/10m_raster ${DISTDIR}/NE2_HR_LC_SR_W_DR.zip

pre-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/naturalearth
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/naturalearth/10m_cultural
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/naturalearth/10m_physical
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/naturalearth/10m_raster

do-install:
	${CP} -pr ${WRKDIR}/naturalearth ${DESTDIR}${PREFIX}/share/

# url2pkg-marker (please do not remove this line.)
.include "../../mk/bsd.pkg.mk"
