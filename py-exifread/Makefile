# $NetBSD$

DISTNAME=	exifread-3.5.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	graphics python
MASTER_SITES=	${MASTER_SITE_PYPI:=E/ExifRead/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/ianare/exif-py
COMMENT=	Read Exif metadata from tiff and jpeg files
LICENSE=	modified-bsd

BUILD_DEPENDS+=	${PYPKGPREFIX}-mypy>=0:../../lang/py-mypy
BUILD_DEPENDS+=	${PYPKGPREFIX}-pylint>=0:../../devel/py-pylint

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

post-install:
	cd ${DESTDIR}${PREFIX}/bin && ${MV} EXIF.py exifread-${PYVERSSUFFIX} || ${TRUE}

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
