# $NetBSD$

DISTNAME=	google_resumable_media-2.8.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_resumable_/-resumable-/}
CATEGORIES=	devel net python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/google_resumable_media/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/google_resumable_media/
COMMENT=	Utilities for Google Media Downloads and Resumable Uploads
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-google-crc32c>=1.0.0:../../pkgsrc_myownpkgs/py-google-crc32c
DEPENDS+=	${PYPKGPREFIX}-requests>=2.18.0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-aiohttp>=3.6.2:../../www/py-aiohttp

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
