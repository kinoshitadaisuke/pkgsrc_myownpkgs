# $NetBSD$

DISTNAME=	astrometry-4.3.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/astrometry/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/astrometry/
COMMENT=	Finding pixel-to-sky transformation for astronomical images
LICENSE=	gnu-gpl-v3

#DISTFILES=				${DEFAULT_DISTFILES}
#DISTFILES+=				astrometry_extension_utilities.h
#SITES.astrometry_extension_utilities.h=	https://raw.githubusercontent.com/neuromorphicsystems/astrometry/main/astrometry_extension/

DEPENDS+=	${PYPKGPREFIX}-setuptools>=50.3.2:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-wheel>0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-astropy>=5.0:../../pkgsrc_myownpkgs/py-astropy

#post-extract:
#	cd ${WRKSRC}/astrometry_extension && ${LN} -s ${WRKDIR}/astrometry_extension_utilities.h

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
