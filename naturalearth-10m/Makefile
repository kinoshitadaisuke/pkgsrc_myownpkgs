# $NetBSD$

DISTNAME=	naturalearth-5.1.1
PKGNAME=	${DISTNAME}
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

NO_BUILD=	yes
EXTRACT_ONLY=	

USE_TOOLS+=	unzip

TOOLS_DEPENDS+=	unzip-[0-9]*:../../archivers/unzip
TOOLS_DEPENDS+=	wget-[0-9]*:../../net/wget

do-install:
	${MKDIR} ${DESTDIR}${PREFIX}/share/naturalearth
	${MKDIR} ${DESTDIR}${PREFIX}/share/naturalearth/10m
	${MKDIR} ${DESTDIR}${PREFIX}/share/naturalearth/10m/10m_physical
	${MKDIR} ${DESTDIR}${PREFIX}/share/naturalearth/10m/10m_raster
	unzip -d ${DESTDIR}${PREFIX}/share/naturalearth/10m ${DISTDIR}/10m_cultural.zip
	unzip -d ${DESTDIR}${PREFIX}/share/naturalearth/10m/10m_physical ${DISTDIR}/10m_physical.zip
	unzip -d ${DESTDIR}${PREFIX}/share/naturalearth/10m/10m_raster ${DISTDIR}/HYP_HR_SR_OB_DR.zip
	unzip -d ${DESTDIR}${PREFIX}/share/naturalearth/10m/10m_raster ${DISTDIR}/NE1_HR_LC_SR_W_DR.zip
	unzip -d ${DESTDIR}${PREFIX}/share/naturalearth/10m/10m_raster ${DISTDIR}/NE2_HR_LC_SR_W_DR.zip
.for datafile in ${DISTFILES}
	${INSTALL_DATA} ${DISTDIR}/${datafile} ${DESTDIR}${PREFIX}/share/naturalearth
.endfor

# url2pkg-marker (please do not remove this line.)
.include "../../mk/bsd.pkg.mk"
